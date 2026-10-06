import sys
import os
import json

from file_utils import file_exists, get_file_size, get_file_extension, get_file_type
from image_analyzer import analyze_image
from video_analyzer import analyze_video
from audio_analyzer import analyze_audio
from report_generator import ReportGenerator
from voice_cloning import clone_voice, list_voices, create_voice_clone, text_to_speech
from image_enhancement import enhance_image_auto, enhance_image_opencv, enhance_image_pil, batch_enhance


def analyze_file(filepath):
    """Analyze metadata of a file based on its type."""
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
        return None, None

    return metadata, report


def save_report(metadata, filename="report.json"):
    """Save metadata report to JSON file."""
    os.makedirs("reports", exist_ok=True)
    report_path = os.path.join("reports", filename)
    with open(report_path, "w") as f:
        json.dump(metadata, f, indent=2)
    print(f"\nReport saved to {report_path}")
    return report_path


def print_usage():
    print("""
Multimedia Analyzer & Enhancement Tool
=======================================

Usage:
  python main.py <command> [arguments]

Commands:
  analyze <file_path>           - Analyze image/video/audio metadata
  enhance <input> <output>      - Enhance image (auto mode)
  enhance-opencv <in> <out>     - Enhance image using OpenCV
  enhance-pil <in> <out>        - Enhance image using PIL
  batch-enhance <in_dir> <out_dir> - Batch enhance images
  tts <text> [output]           - Text to speech (requires ELEVENLABS_API_KEY)
  clone-voice <text> [output]   - Voice cloning (requires ELEVENLABS_API_KEY)
  list-voices                   - List available voices (requires ELEVENLABS_API_KEY)
  create-voice <name> <audio_files...> - Create custom voice clone

Environment Variables:
  ELEVENLABS_API_KEY - Your ElevenLabs API key (get from https://elevenlabs.io)

Examples:
  python main.py analyze samples/image.jpg
  python main.py enhance samples/image.jpg output/enhanced.jpg
  python main.py batch-enhance samples/ output/
  python main.py tts "Hello world" output/speech.mp3
  python main.py clone-voice "Hello from cloned voice" output/cloned.mp3
  python main.py list-voices
""")


def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1]

    if command == "analyze":
        if len(sys.argv) < 3:
            print("Usage: python main.py analyze <file_path>")
            sys.exit(1)
        
        filepath = sys.argv[2]
        if not file_exists(filepath):
            print(f"Error: File '{filepath}' does not exist.")
            sys.exit(1)

        metadata, report = analyze_file(filepath)
        if metadata is None:
            sys.exit(1)

        print(report)
        save_report(metadata)

    elif command == "enhance":
        if len(sys.argv) < 4:
            print("Usage: python main.py enhance <input> <output> [method]")
            print("Methods: auto (default), pil, opencv")
            sys.exit(1)
        
        input_path = sys.argv[2]
        output_path = sys.argv[3]
        method = sys.argv[4] if len(sys.argv) > 4 else "auto"
        
        if not file_exists(input_path):
            print(f"Error: File '{input_path}' does not exist.")
            sys.exit(1)

        print(f"Enhancing image using {method}...")
        result = enhance_image_auto(input_path, output_path, method)
        
        if result["status"] == "success":
            print(f"Success! Enhanced image saved to: {output_path}")
            print(f"Enhancements applied: {result['enhancements_applied']}")
        else:
            print(f"Error: {result['message']}")
            sys.exit(1)

    elif command == "enhance-opencv":
        if len(sys.argv) < 4:
            print("Usage: python main.py enhance-opencv <input> <output>")
            sys.exit(1)
        
        input_path = sys.argv[2]
        output_path = sys.argv[3]
        
        if not file_exists(input_path):
            print(f"Error: File '{input_path}' does not exist.")
            sys.exit(1)

        result = enhance_image_opencv(input_path, output_path)
        if result["status"] == "success":
            print(f"Success! Enhanced image saved to: {output_path}")
        else:
            print(f"Error: {result['message']}")
            sys.exit(1)

    elif command == "enhance-pil":
        if len(sys.argv) < 4:
            print("Usage: python main.py enhance-pil <input> <output>")
            sys.exit(1)
        
        input_path = sys.argv[2]
        output_path = sys.argv[3]
        
        if not file_exists(input_path):
            print(f"Error: File '{input_path}' does not exist.")
            sys.exit(1)

        result = enhance_image_pil(input_path, output_path)
        if result["status"] == "success":
            print(f"Success! Enhanced image saved to: {output_path}")
        else:
            print(f"Error: {result['message']}")
            sys.exit(1)

    elif command == "batch-enhance":
        if len(sys.argv) < 4:
            print("Usage: python main.py batch-enhance <input_dir> <output_dir> [method]")
            sys.exit(1)
        
        input_dir = sys.argv[2]
        output_dir = sys.argv[3]
        method = sys.argv[4] if len(sys.argv) > 4 else "pil"
        
        if not os.path.isdir(input_dir):
            print(f"Error: Directory '{input_dir}' does not exist.")
            sys.exit(1)

        print(f"Batch enhancing images in {input_dir}...")
        result = batch_enhance(input_dir, output_dir, method)
        
        if result["status"] == "success":
            print(f"Processed {result['processed']} images")
            for r in result["results"]:
                if r["status"] == "success":
                    print(f"  ✓ {r['output_path']}")
                else:
                    print(f"  ✗ {r.get('message', 'Unknown error')}")
        else:
            print(f"Error: {result['message']}")
            sys.exit(1)

    elif command in ("tts", "text-to-speech", "clone-voice"):
        api_key = os.environ.get("ELEVENLABS_API_KEY")
        if not api_key:
            print("Error: ELEVENLABS_API_KEY environment variable not set.")
            print("Get your API key from https://elevenlabs.io")
            sys.exit(1)

        if len(sys.argv) < 3:
            print(f"Usage: python main.py {command} <text> [output_path]")
            sys.exit(1)

        text = sys.argv[2]
        output_path = sys.argv[3] if len(sys.argv) > 3 else "output_speech.mp3"

        print(f"Generating speech for: '{text}'...")
        result = clone_voice(api_key, text, output_path=output_path)

        if result["status"] == "success":
            print(f"Success! Audio saved to: {result['output_path']}")
            print(f"Voice ID: {result['voice_id']}")
            print(f"Model: {result['model_id']}")
        else:
            print(f"Error: {result['message']}")
            sys.exit(1)

    elif command == "list-voices":
        api_key = os.environ.get("ELEVENLABS_API_KEY")
        if not api_key:
            print("Error: ELEVENLABS_API_KEY environment variable not set.")
            sys.exit(1)

        result = list_voices(api_key)
        if result["status"] == "success":
            print("Available Voices:")
            for v in result["voices"]:
                print(f"  - {v['name']} (ID: {v['voice_id']}) - {v['category']}")
        else:
            print(f"Error: {result['message']}")
            sys.exit(1)

    elif command == "create-voice":
        api_key = os.environ.get("ELEVENLABS_API_KEY")
        if not api_key:
            print("Error: ELEVENLABS_API_KEY environment variable not set.")
            sys.exit(1)

        if len(sys.argv) < 4:
            print("Usage: python main.py create-voice <name> <audio_file1> [audio_file2] ...")
            sys.exit(1)

        name = sys.argv[2]
        audio_files = sys.argv[3:]

        for f in audio_files:
            if not file_exists(f):
                print(f"Error: File '{f}' does not exist.")
                sys.exit(1)

        print(f"Creating voice clone '{name}' from {len(audio_files)} audio file(s)...")
        result = create_voice_clone(api_key, name, audio_files)

        if result["status"] == "success":
            print(f"Success! Voice created with ID: {result['voice_id']}")
        else:
            print(f"Error: {result['message']}")
            sys.exit(1)

    else:
        print(f"Unknown command: {command}")
        print_usage()
        sys.exit(1)


if __name__ == "__main__":
    main()