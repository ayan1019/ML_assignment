
# 🎙️ Voice Cloning & Video Processing Pipeline — ML Assignment Project

This project implements a complete video preprocessing, transcription, face detection, and **English voice cloning** pipeline using state-of-the-art models like Whisper (OpenAI), MediaPipe, and XTTS-v2 (Coqui). It is exposed via a **FastAPI** backend with endpoints to upload a video, check job status, and download final results (audio + transcript).

---

## 📌 Features

- ✅ Extract frames and faces from a video
- ✅ Extract and transcribe audio using **Whisper**
- ✅ Clone the voice from the video using **XTTS-v2**
- ✅ Generate new audio with cloned voice speaking the transcript
- ✅ FastAPI server with REST endpoints: `/upload`, `/status/{job_id}`, `/result/{job_id}`

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clonehttps://github.com/ayan1019/ML_assignment.git
cd ML_assignment
```

### 2. Create & Activate Virtual Environment

```bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Install & Setup FFmpeg (macOS)

```bash
brew install ffmpeg

```
(For Windows: install from https://ffmpeg.org/download.html and add it to PATH)


### 🤖 Models Used

```
| Task           | Model                    |
| -------------- | ------------------------ |
| ASR            | Whisper (base)           |
| Face Detection | MediaPipe Face Detection |
| Voice Cloning  | XTTS-v2 (English only)   |

```

### 🚀 Running the API
#### Start the FastAPI server
```bash
uvicorn app.main:app --reload
```

### Available Endpoints
```
| Method | Endpoint       | Description                             |
| ------ | -------------- | --------------------------------------- |
| POST   | `/upload`      | Upload a `.mp4` video for processing    |
| GET    | `/status/{id}` | Check processing status of a job        |
| GET    | `/result/{id}` | Get transcript, cloned audio, and video |
```

### 📄 Sample API Calls
#### Upload a video
```
curl -X POST http://localhost:8000/upload \
  -F "file=@sample_video.mp4"
```

### Check status
```
curl http://localhost:8000/status/1234abcd

```

### Get result
```
curl hcurl http://localhost:8000/result/1234abcd

```

### ✅ Status
✅ Complete pipeline integrated with FastAPI

✅ Modular, extensible, and ready for production-level scaling

### 👨‍💻 Author
#### Ayan Yadav
#### Data Science & AI Enthusiast


