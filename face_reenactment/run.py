import subprocess
from loguru import logger

def run_face_reenactment(
    source_image="output/frames/frame_0000.jpg",
    driving_video="LivePortrait/assets/examples/driving/d9.mp4",
    checkpoint="LivePortrait/checkpoints/liveportrait.pth.tar",
    result_dir="output"
):
    logger.info("Running face reenactment using LivePortrait (KwaiVGI version)...")

    command = [
    "python3", "LivePortrait/inference.py",
    "--source", source_image,
    "--driving", driving_video,
    "--checkpoint-path", checkpoint,
    "--output-dir", result_dir,
    "--flag-relative-motion",
    "--flag-do-crop",
    "--flag-crop-driving-video"
]
    print("Running command:", " ".join(command))


    try:
        subprocess.run(command, check=True)
        logger.success("Face reenactment completed successfully!")
    except subprocess.CalledProcessError as e:
        logger.error(f"Face reenactment failed: {e}")
