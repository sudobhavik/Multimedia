import os
from moviepy import AudioFileClip


def analyze_audio(filepath: str) -> dict:
    file_size = os.path.getsize(filepath)

    codec = "Unknown"
    channels = None
    sampling_rate = None
    bitrate = None
    duration = 0

    try:
        with AudioFileClip(filepath) as audio:
            duration = audio.duration
            channels = audio.nchannels
            sampling_rate = audio.fps
            if hasattr(audio.reader, "codec") and audio.reader.codec:
                codec = audio.reader.codec
            if hasattr(audio.reader, "bitrate") and audio.reader.bitrate:
                bitrate = audio.reader.bitrate
    except Exception:
        duration = 0
        channels = 0
        sampling_rate = 0

    return {
        "file_name": os.path.basename(filepath),
        "file_size": file_size,
        "duration": duration,
        "codec": codec,
        "channels": channels,
        "sampling_rate": sampling_rate,
        "bitrate": bitrate,
    }
