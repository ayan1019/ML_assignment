import requests

video_path = "test_video.mp4"
with open(video_path, "rb") as f:
    res = requests.post("http://localhost:8000/upload", files={"file": f})

job_id = res.json()["job_id"]
print("Job ID:", job_id)

# Check status
status = requests.get(f"http://localhost:8000/status/{job_id}").json()
print("Status:", status)

# Get result (once status is "done")
result = requests.get(f"http://localhost:8000/result/{job_id}").json()
print("Result:", result)
