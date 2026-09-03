import sys
import os

from file_utils import file_exists, get_file_size, get_file_extension, get_file_type
from image_analyzer import analyze_image
from video_analyzer import analyze_video
from audio_analyzer import analyze_audio
from report_generator import ReportGenerator


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)

    filepath = sys.argv[1]

    if not file_exists(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        sys.exit(1)

    file_ext = get_file_extension(filepath)
    file_type = get_file_type(filepath)

    metadata = {"file_type": file_type, "file_name": os.path.basename(filepath)}

    if file_ext in (".jpg", ".jpeg", ".png", ".tiff", ".tif", ".webp", ".bmp"):
        result = analyze_image(filepath)
        metadata.update(result)
        report = ReportGenerator.generate_image_report(metadata)
    elif file_ext in (".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv"):
        result = analyze_video(filepath)
        metadata.update(result)
        report = ReportGenerator.generate_video_report(metadata)
    elif file_ext in (".mp3", ".wav", ".flac", ".aac", ".wma"):
        result = analyze_audio(filepath)
        metadata.update(result)
        report = ReportGenerator.generate_audio_report(metadata)
    else:
        print(f"Unsupported file format: {file_ext}")
        sys.exit(1)

    print(report)

    os.makedirs("reports", exist_ok=True)
    with open("reports/report.json", "w") as f:
        import json
        json.dump(metadata, f, indent=2)

    print(f"\nReport saved to reports/report.json")


if __name__ == "__main__":
    main()