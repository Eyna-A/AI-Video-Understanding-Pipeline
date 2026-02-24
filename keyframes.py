import cv2
import os
import numpy as np


def extract_keyframes(video_path: str, threshold=30, max_frames=5):
    os.makedirs("data/keyframes", exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)

    keyframes = []
    prev_gray = None
    count = 0

    while cap.isOpened() and len(keyframes) < max_frames:
        ok, frame = cap.read()
        if not ok:
            break

        count += 1

        if count % int(fps) != 0:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if prev_gray is not None:
            diff = np.mean(cv2.absdiff(prev_gray, gray))
            if diff > threshold:
                path = f"data/keyframes/frame_{len(keyframes)}.jpg"
                cv2.imwrite(path, frame)

                keyframes.append({
                    "path": path,
                    "timestamp": count / fps
                })

        prev_gray = gray

    cap.release()
    return keyframes
