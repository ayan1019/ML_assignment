from preprocessing.extract_pipeline import extract_frames, extract_audio, detect_faces, transcribe_audio
from face_reenactment.run import run_face_reenactment

video_path = "test_video.mp4"
extract_frames(video_path)
extract_audio(video_path)
detect_faces()
transcribe_audio()
run_face_reenactment()