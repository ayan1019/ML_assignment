from TTS.api import TTS
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs  # ✅ Add XttsArgs
from TTS.config.shared_configs import BaseDatasetConfig
from torch.serialization import add_safe_globals
import os

# ✅ Allow all necessary globals for loading the model config
add_safe_globals([XttsConfig, XttsAudioConfig, BaseDatasetConfig, XttsArgs])



# Init the model (downloaded automatically)
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=True, gpu=False)

# Paths
reference_audio_path = "output/audio.wav"   # Your speaker's reference audio
with open("output/transcript.txt", "r") as f:
    text = f.read()
output_path = "output/cloned_output.wav"

# Run synthesis
tts.tts_to_file(
    text=text,
    speaker_wav=reference_audio_path,
    language="en",  # English output
    file_path=output_path
)

print(f"✅ Cloned speech saved to {output_path}")
