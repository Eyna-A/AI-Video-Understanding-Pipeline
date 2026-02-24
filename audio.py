import os
from moviepy import VideoFileClip


def extract_audio(video_path, output_path="data/audio/audio.wav"):
    # حتماً پوشه ساخته شود (جلوگیری از BrokenPipe در ویندوز)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    clip = VideoFileClip(video_path)

    if clip.audio is None:
        raise RuntimeError("Video has no audio track")

    clip.audio.write_audiofile(output_path)

    clip.close()

    return output_path

