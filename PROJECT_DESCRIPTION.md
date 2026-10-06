# Multimedia Analyzer and Enhancement Tool

## 1. Project Overview

This project is a Python-based multimedia utility designed to analyze and enhance different types of media files such as images, audio, and video. It can extract metadata, generate structured reports, improve image quality, and integrate with ElevenLabs for voice cloning and text-to-speech functionalities.

The repository is built around a simple command-line interface (CLI), where users can run commands like:

- analyze an image, video, or audio file
- enhance an image using PIL or OpenCV
- process multiple images in a batch
- generate speech from text
- create or list voices through the ElevenLabs API

The main entry point is the file `main.py`, and the actual implementation logic is separated into modules under `src/`.

---

## 2. What This Project Does

The project provides five major features:

1. Image metadata analysis
   - Reads image dimensions, format, color mode, and EXIF data
   - Identifies width, height, file type, and metadata information

2. Video metadata analysis
   - Reads video duration, resolution, frame rate, codec, and audio properties
   - Works through MoviePy's VideoFileClip API

3. Audio metadata analysis
   - Reads audio duration, sample rate, bitrate, channel count, and codec information

4. Image enhancement
   - Improves image appearance using either Pillow (PIL) or OpenCV
   - Supports batch enhancement as well

5. Voice cloning and text-to-speech
   - Uses the ElevenLabs API to generate audio from text
   - Allows listing existing voices and creating custom voice clones from sample recordings

---

## 3. Technologies and Libraries Used

The project uses Python and several third-party packages from `requirements.txt`:

- `pillow>=11.0.0`
  - Used for PIL-based image processing and enhancement
  - Helps read image properties and manipulate images

- `moviepy>=2.0.0`
  - Used to process audio and video files
  - Extracts metadata like duration, fps, codecs, channels, and bitrate

- `opencv-python-headless>=4.8.0`
  - Used for advanced image enhancement tasks
  - Handles denoising, sharpening, saturation, and contrast adjustments

- `elevenlabs>=2.0.0`
  - Used for AI voice generation and voice management
  - Connects to ElevenLabs for text-to-speech and voice cloning

- `numpy>=1.24.0`
  - Used to support image processing operations in OpenCV calculations

These libraries are defined in the file:

- `requirements.txt`

---

## 4. Repository Structure

The project layout is as follows:

```text
Multimedia/
├── main.py                     # Main CLI entry point
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
├── .env.example                # Example environment variables
├── samples/                    # Example media files for testing
│   ├── image.jpg
│   ├── video.mp4
│   ├── song.mp3
│   ├── song.wav
│   └── other sample media files
├── reports/                    # Output generated JSON metadata reports
├── src/                        # Source code modules
│   ├── file_utils.py           # Utility functions for files
│   ├── image_analyzer.py       # Image analysis logic
│   ├── video_analyzer.py       # Video analysis logic
│   ├── audio_analyzer.py       # Audio analysis logic
│   ├── report_generator.py     # Console report formatting
│   ├── image_enhancement.py    # PIL/OpenCV enhancement methods
│   ├── voice_cloning.py        # ElevenLabs API integration
│   ├── main.py                 # Alternative or module-level CLI logic
│   ├── Cluster01-Multimedia-Fundamentals/
│   ├── Cluster02-Image-Processing/
│   ├── Cluster03-Audio-Processing/
│   └── Cluster04-Video-Processing/
└── __pycache__/                # Python-generated cache files
```

---

## 5. Where Everything Is Implemented

### 5.1 Main application entry
File: `main.py`

This file is the project entry point. It does the following:

- adds `src` to the Python import path
- imports all required modules
- handles command-line arguments
- dispatches the correct function depending on the user command
- validates files and directories
- saves reports as JSON files

This is where the user interacts with the application as a CLI tool.

### 5.2 File utility helpers
File: `src/file_utils.py`

This file contains reusable functions such as:

- `file_exists(filepath)`
- `get_file_size(filepath)`
- `get_file_extension(filepath)`
- `get_file_type(filepath)`

These are used by the main CLI and analysis functions to check whether files exist and identify file types based on their extension.

### 5.3 Image analysis
File: `src/image_analyzer.py`

This module reads image files using Pillow.

Functions implemented:

- `analyze_image(filepath: str) -> dict`

It returns a dictionary containing:

- file name
- file size
- file format
- width
- height
- color mode
- EXIF metadata

It uses:

- `Image.open(filepath)`
- `img.size` for dimensions
- `img.mode` for color mode
- `img.getexif()` for metadata extraction

### 5.4 Audio analysis
File: `src/audio_analyzer.py`

This module extracts metadata from audio files using MoviePy.

Function:

- `analyze_audio(filepath: str) -> dict`

It obtains:

- duration
- number of channels
- sampling rate
- codec
- bitrate

It uses `AudioFileClip` from `moviepy` to read audio details.

### 5.5 Video analysis
File: `src/video_analyzer.py`

This module analyzes videos using `VideoFileClip`.

Function:

- `analyze_video(filepath: str) -> dict`

It extracts:

- duration
- video resolution
- FPS
- container type
- frame rate
- video codec
- audio codec
- audio channel count
- audio bitrate

### 5.6 Report generation
File: `src/report_generator.py`

This module formats results for display in the terminal.

It includes:

- `generate_image_report(metadata)`
- `generate_video_report(metadata)`
- `generate_audio_report(metadata)`
- `generate_report(metadata)`

These methods create readable console output with sections for file metadata.

### 5.7 Image enhancement
File: `src/image_enhancement.py`

This module contains enhancement logic for images.

Functions:

- `enhance_image_opencv(input_path, output_path, enhancements=None)`
- `enhance_image_pil(input_path, output_path, enhancements=None)`
- `enhance_image_auto(input_path, output_path, method="pil")`
- `batch_enhance(input_dir, output_dir, method="pil")`

It enhances images using:

- OpenCV for denoising, sharpening, contrast, brightness, and saturation
- PIL for brightness, contrast, sharpness, color, and median filtering

The auto mode chooses a sensible enhancement strategy depending on the selected backend.

### 5.8 Voice cloning and TTS
File: `src/voice_cloning.py`

This file connects the application to ElevenLabs services.

Functions:

- `clone_voice(api_key, text, voice_id=None, output_path="output_audio.mp3", model_id="eleven_multilingual_v2")`
- `create_voice_clone(api_key, name, audio_files, description="")`
- `list_voices(api_key)`
- `text_to_speech(api_key, text, voice_id=None, output_path="output.mp3")`

It uses:

- `ElevenLabs(api_key=api_key)`
- `client.text_to_speech.convert(...)`
- `save(audio, output_path)`

This feature allows AI-generated voice output and custom voice creation from recorded samples.

---

## 6. How the Project Works

### 6.1 Command-line workflow
The app works through text commands executed in the terminal.

Example commands:

```bash
python main.py analyze samples/image.jpg
python main.py analyze samples/video.mp4
python main.py analyze samples/song.wav
python main.py enhance samples/image.jpg output/enhanced.jpg auto
python main.py batch-enhance samples/ output/batch/ pil
python main.py tts "Hello world" output/speech.mp3
python main.py list-voices
python main.py create-voice "MyVoice" sample1.wav sample2.wav
```

The CLI checks the first argument, which identifies the command. Then it validates the input and calls the corresponding function.

### 6.2 Analyze flow
When `analyze` is triggered:

1. The file path is read from the command line
2. It checks whether the file exists by calling `file_exists()`
3. It identifies the extension with `get_file_extension()`
4. It identifies the file type with `get_file_type()`
5. Based on extension, it calls:
   - `analyze_image()` for image files
   - `analyze_video()` for video files
   - `analyze_audio()` for audio files
6. The result is merged into a metadata dictionary
7. A report is generated using `ReportGenerator`
8. The final output is printed to the console
9. JSON is saved into `reports/report.json`

### 6.3 Enhancement flow
When `enhance` or `batch-enhance` is triggered:

1. The input file or directory is validated
2. Images are opened using PIL or OpenCV
3. Enhancement operations are applied
4. The processed image is saved to the output location
5. A result dictionary is returned containing success or failure details

### 6.4 Voice cloning flow
When the TTS or voice cloning features are used:

1. The API key is read from environment variables
2. A client is created using ElevenLabs
3. The requested text is sent to the API
4. A voice model is selected
5. The generated speech is saved as an audio file
6. Metadata like voice ID and model ID are returned

---

## 7. How the Project Is Structured Logically

The project follows a modular architecture:

- `main.py` = CLI orchestrator
- `src/file_utils.py` = common utility layer
- `src/<media>_analyzer.py` = media-specific extraction logic
- `src/report_generator.py` = output formatting layer
- `src/image_enhancement.py` = enhancement operations
- `src/voice_cloning.py` = external API integration

This separation keeps the project organized and makes it easier to add new media types or features later.

---

## 8. Important Implementation Details

### File type detection
The project detects file type using extension and MIME mapping.

This is implemented in `src/file_utils.py` via:

- `get_file_extension(filepath)`
- `get_file_type(filepath)`

These functions use Python's `os.path.splitext()` and `mimetypes.guess_type()`.

### Report saving
The `save_report()` function creates a `reports` directory if it does not already exist and writes the JSON metadata to a file called `report.json`.

### Input validation
The CLI checks for:

- nonexistent files
- invalid commands
- missing arguments
- missing environment variable `ELEVENLABS_API_KEY` when prompting AI voice features

### Error handling
The project prints friendly error messages and exits with non-zero status when something fails.

---

## 9. Practical Example: Image Analysis

For example, if the user runs:

```bash
python main.py analyze samples/image.jpg
```

The app:

1. validates the file path
2. calls `analyze_image()`
3. reads the image with Pillow
4. extracts EXIF and image properties
5. creates a report with width, height, format, and color mode
6. stores metadata in `reports/report.json`

---

## 10. Practical Example: Voice Cloning

For example, if the user runs:

```bash
python main.py tts "Hello world" output/speech.mp3
```

The project expects the environment variable `ELEVENLABS_API_KEY` to be set.

Then it:

1. creates an ElevenLabs client
2. selects a voice
3. sends the text to the API
4. receives audio synthesis output
5. saves the generated MP3 file to `output/speech.mp3`

---

## 11. Notes About the Project

This repository is a practical multimedia project that combines:

- metadata extraction
- media enhancement
- AI-based voice generation
- Python CLI design
- modular code organization

It is suitable for education, assignments, experimentation, and simple multimedia processing workflows.

The project also includes cluster-based examples under `src/Cluster*` folders, showing different implementations of similar tasks for different media categories.

---

## 12. Summary

In short, this project is a Python-based multimedia toolkit that allows users to:

- inspect files,
- understand their metadata,
- improve image quality,
- generate AI voice outputs,
- and save structured reports.

It is implemented through a clean separation of concerns, where each media type and feature is handled by dedicated modules inside the `src/` directory, and the CLI in `main.py` acts as the main coordinator.

---

## 13. Main Files to Remember

- `main.py` — main command-line entry point
- `src/file_utils.py` — common file helpers
- `src/image_analyzer.py` — image metadata extraction
- `src/video_analyzer.py` — video metadata extraction
- `src/audio_analyzer.py` — audio metadata extraction
- `src/report_generator.py` — metadata report formatting
- `src/image_enhancement.py` — enhancement features
- `src/voice_cloning.py` — AI voice integration
- `requirements.txt` — project dependencies
- `README.md` — user-facing documentation

This project is a complete multimedia analyzer and enhancement toolkit built in Python, using strong modular design and versatile media processing libraries.
