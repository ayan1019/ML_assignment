import os
import cv2
import ffmpeg
import whisper
import mediapipe as mp
from loguru import logger
from pathlib import Path
import glob

# Output directories
BASE_OUTPUT = Path("output")
FRAMES_DIR = BASE_OUTPUT / "frames"
AUDIO_PATH = BASE_OUTPUT / "audio.wav"
TRANSCRIPT_PATH = BASE_OUTPUT / "transcript.txt"

# Setup logging
logger.add("logs/preprocessing.log", rotation="500 KB")

def extract_frames(video_path):
    logger.info("Starting frame extraction...")
    os.makedirs(FRAMES_DIR, exist_ok=True)

    cap = cv2.VideoCapture(str(video_path))
    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_path = FRAMES_DIR / f"frame_{i:04d}.jpg"
        cv2.imwrite(str(frame_path), frame)
        i += 1

    cap.release()
    logger.success(f"Extracted {i} frames to {FRAMES_DIR}")

def extract_audio(video_path):
    logger.info("Extracting audio from video...")
    os.makedirs(BASE_OUTPUT, exist_ok=True)
    try:
        ffmpeg.input(str(video_path)).output(
            str(AUDIO_PATH), ar=16000, ac=1, format='wav'
        ).overwrite_output().run(quiet=True)
        logger.success(f"Saved audio to {AUDIO_PATH}")
    except ffmpeg.Error as e:
        logger.error(f"ffmpeg error: {e.stderr}")

def detect_faces():
    logger.info("Detecting faces in frames...")
    mp_face = mp.solutions.face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5)

    for frame_path in sorted(FRAMES_DIR.glob("*.jpg")):
        image = cv2.imread(str(frame_path))
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = mp_face.process(rgb_image)
        if results.detections:
            logger.info(f"✔️ Face detected in {frame_path.name}")
        else:
            logger.warning(f"❌ No face in {frame_path.name}")

def transcribe_audio():
    logger.info("Transcribing audio with Whisper...")
    model = whisper.load_model("base")
    result = model.transcribe(str(AUDIO_PATH))
    with open(TRANSCRIPT_PATH, "w") as f:
        f.write(result["text"])
    logger.success(f"Transcription saved to {TRANSCRIPT_PATH}")
