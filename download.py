import os
import subprocess


def download_video(url, output_path="data/videos/video.mp4"):
    # مطمئن شو پوشه وجود دارد
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    cmd = [
        "yt-dlp",
        "-f", "bestaudio+bestvideo",
        "-o", output_path,
        "--no-playlist",
        url,
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        return output_path

    raise RuntimeError(f"Video download failed: {result.stderr}")
