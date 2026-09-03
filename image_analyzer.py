import os
from PIL import Image
from PIL.ExifTags import TAGS


def analyze_image(filepath: str) -> dict:
    file_size = os.path.getsize(filepath)
    ext = os.path.splitext(filepath)[1].lower()

    with Image.open(filepath) as img:
        width, height = img.size
        color_mode = img.mode

        exif_data = {}
        exif = img.getexif()
        for tag_id, value in exif.items():
            tag_name = TAGS.get(tag_id, tag_id)
            exif_data[tag_name] = value

        return {
            "file_name": os.path.basename(filepath),
            "file_size": file_size,
            "file_format": img.format if img.format else "",
            "width": width,
            "height": height,
            "color_mode": color_mode,
            "exif": exif_data,
        }