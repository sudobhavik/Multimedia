import os
import mimetypes


def file_exists(filepath: str) -> bool:
    return os.path.isfile(filepath)


def get_file_size(filepath: str) -> int:
    return os.path.getsize(filepath)


def get_file_extension(filepath: str) -> str:
    _, ext = os.path.splitext(filepath)
    return ext.lower()


def get_file_type(filepath: str) -> str:
    _, ext = os.path.splitext(filepath)
    ext = ext.lower()
    mime_type, _ = mimetypes.guess_type(filepath)
    if mime_type:
        return mime_type
    return f"application/{ext}" if ext else "application/octet-stream"
