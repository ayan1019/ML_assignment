
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil
import subprocess
import os

from api.job_manager import create_job, update_job_status, set_job_output, get_job_status, get_job_result

app = FastAPI()
UPLOAD_DIR = Path("uploads")
OUTPUT_DIR = Path("output")
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

@app.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    job_id = create_job()
    update_job_status(job_id, "processing")

    video_path = UPLOAD_DIR / f"{job_id}_{file.filename}"
    with open(video_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Run pipeline
    try:
        subprocess.run(["python", "preprocessing/extract_pipeline.py", str(video_path)], check=True)
        subprocess.run(["python", "clone_with_xtts.py"], check=True)
    except subprocess.CalledProcessError as e:
        update_job_status(job_id, "error")
        return JSONResponse(status_code=500, content={"error": str(e)})

    # Save final output details
    output = {
        "audio": str(OUTPUT_DIR / "cloned_output.wav"),
        "transcript": str(OUTPUT_DIR / "transcript.txt")
    }
    set_job_output(job_id, output)

    return {"job_id": job_id}

@app.get("/status/{job_id}")
def check_status(job_id: str):
    return get_job_status(job_id)

@app.get("/result/{job_id}")
def get_result(job_id: str):
    result = get_job_result(job_id)
    if not result:
        return JSONResponse(status_code=404, content={"error": "Result not ready or job not found"})
    return result
