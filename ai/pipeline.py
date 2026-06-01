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

    #  Download video
    video_path = download_video(video_url)

    #  Extract audio
    audio_path = extract_audio(video_path)

    #  Speech → Text
    transcript, language = speech_to_text(audio_path)

    #  Generate summary
    summary = translate_and_structure(transcript)

    #  Return clean contract 
    return {
        "status": "success",
        "summary": summary,
        "transcript": transcript
    }

