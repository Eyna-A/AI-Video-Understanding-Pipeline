import whisper
import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

model = whisper.load_model("base", device=DEVICE)


def speech_to_text(audio_path: str):
    result = model.transcribe(audio_path)

    text = result["text"].strip()
    language = result.get("language", "unknown")

    return text, language
