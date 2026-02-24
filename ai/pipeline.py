from .download import download_video
from .audio import extract_audio
from .transcribe import speech_to_text
from .summarize import translate_and_structure


def process_video(video_url: str) -> dict:
    """
    Main AI entry point.
    Called by Backend.
    Must return ONLY what backend needs.
    """

    # 1️⃣ Download video
    video_path = download_video(video_url)

    # 2️⃣ Extract audio
    audio_path = extract_audio(video_path)

    # 3️⃣ Speech → Text
    transcript, language = speech_to_text(audio_path)

    # 4️⃣ Generate summary (inside summarize module)
    summary = translate_and_structure(transcript)

    # 5️⃣ Return clean contract (NO extra data)
    return {
        "status": "success",
        "summary": summary,
        "transcript": transcript
    }

