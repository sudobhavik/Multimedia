import os
from moviepy import VideoFileClip


def analyze_video(filepath: str) -> dict:
    file_size = os.path.getsize(filepath)

    with VideoFileClip(filepath) as clip:
        duration = clip.duration
        resolution = clip.size
        fps = clip.fps
        container = os.path.splitext(filepath)[1].lower().lstrip('.')

        # Get bitrate from the video file metadata if available
        bitrate = None
        try:
            # Try to get bitrate from the underlying ffmpeg reader
            bitrate = clip.reader.metadata.get('bitrate')
        except Exception:
            pass

        audio = clip.audio
        codec = audio.codec if audio else None
        channels = audio.nchannels if audio else None
        sampling_rate = audio.fps if audio else None
        audio_bitrate = audio.bitrate if audio else None

    return {
        "file_name": os.path.basename(filepath),
        "file_size": file_size,
        "container": container,
        "duration": duration,
        "resolution": resolution,
        "frame_rate": fps,
        "bit_rate": bitrate,
        "codec": codec,
        "audio_codec": audio.codec if audio else None,
        "audio_channels": audio.nchannels if audio else None,
        "audio_sampling_rate": audio.fps if audio else None,
        "audio_bitrate": audio.bitrate if audio else None,
    }