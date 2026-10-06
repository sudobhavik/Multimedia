# Multimedia Analyzer & Enhancement Tool

A comprehensive Python tool for multimedia file analysis and enhancement with the following capabilities:

## Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | **Image Metadata Analyzer** | Extract EXIF, dimensions, color mode, format info |
| 2 | **Video Metadata Analyzer** | Extract resolution, fps, duration, codecs, bitrates |
| 3 | **Audio Metadata Analyzer** | Extract duration, sample rate, channels, codec, bitrate |
| 4 | **Voice Cloning (ElevenLabs)** | Text-to-speech, custom voice creation, voice listing |
| 5 | **Image Enhancement** | Auto-enhance, OpenCV & PIL backends, batch processing |

## Project Structure

```
multimedia-tool/
├── main.py                    # Entry point (run from here)
├── README.md                  # This file
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variable template
├── samples/                  # Sample media files
│   ├── image.jpg
│   ├── video.mp4
│   ├── song.mp3
│   └── song.wav
├── src/                      # Source code modules
│   ├── file_utils.py         # File utilities
│   ├── image_analyzer.py     # Image metadata extraction
│   ├── video_analyzer.py     # Video metadata extraction
│   ├── audio_analyzer.py     # Audio metadata extraction
│   ├── report_generator.py   # Report formatting
│   ├── voice_cloning.py      # ElevenLabs integration
│   ├── image_enhancement.py  # Image enhancement (OpenCV + PIL)
│   └── Cluster*/             # Original cluster implementations
├── output/                   # Generated outputs (gitignored)
├── reports/                  # JSON reports (gitignored)
└── venv/                     # Virtual environment (gitignored)
```

## Quick Start

### 1. Setup Environment

```bash
# Clone/navigate to project
cd /home/artistbhavik/MM

# Create virtual environment (if not exists)
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Key

```bash
# Copy example env file
cp .env.example .env

# Edit .env and add your ElevenLabs API key
# ELEVENLABS_API_KEY=sk_47e00893b640440d5aa949eb0faa003ce55b98b9dc5a8037
```

Or export directly:
```bash
export ELEVENLABS_API_KEY=sk_47e00893b640440d5aa949eb0faa003ce55b98b9dc5a8037
```

### 3. Run Commands

```bash
# Show help
python main.py

# Analyze metadata
python main.py analyze samples/image.jpg
python main.py analyze samples/video.mp4
python main.py analyze samples/song.wav

# Enhance images
python main.py enhance samples/image.jpg output/enhanced.jpg auto
python main.py enhance-opencv samples/image.jpg output/enhanced_cv.jpg
python main.py enhance-pil samples/image.jpg output/enhanced_pil.jpg

# Batch enhance
python main.py batch-enhance samples/ output/batch/ pil

# Voice cloning (requires API key)
python main.py tts "Hello world" output/speech.mp3
python main.py clone-voice "Hello from cloned voice" output/cloned.mp3
python main.py list-voices
python main.py create-voice "MyVoice" samples/voice1.wav samples/voice2.wav
```

## Detailed Usage

### Metadata Analysis

Extract comprehensive metadata from images, videos, and audio files.

```bash
# Image analysis - shows dimensions, format, color mode, EXIF data
python main.py analyze samples/image.jpg

# Video analysis - shows resolution, FPS, duration, codecs
python main.py analyze samples/video.mp4

# Audio analysis - shows duration, sample rate, channels, bitrate
python main.py analyze samples/song.wav
```

**Output:** Console report + JSON saved to `reports/report.json`

### Image Enhancement

Three enhancement backends available:

| Method | Description | Best For |
|--------|-------------|----------|
| `auto` | Smart defaults (PIL-based) | General use |
| `pil` | Pillow enhancements | Color/contrast tweaks |
| `opencv` | OpenCV processing | Denoising, sharpening, super-res |

```bash
# Auto-enhance (recommended)
python main.py enhance input.jpg output/enhanced.jpg auto

# OpenCV backend (denoise, sharpen, contrast, saturation)
python main.py enhance-opencv input.jpg output/enhanced.jpg

# PIL backend (brightness, contrast, sharpness, color)
python main.py enhance-pil input.jpg output/enhanced.jpg

# Batch process directory
python main.py batch-enhance input_folder/ output_folder/ pil
```

**OpenCV Enhancements:**
- Non-local means denoising
- Unsharp masking (sharpening)
- Contrast/brightness adjustment
- HSV saturation control
- Optional super-resolution upscaling

**PIL Enhancements:**
- Contrast enhancement
- Brightness adjustment
- Sharpness enhancement
- Color/saturation boost
- Median filter denoising

### Voice Cloning (ElevenLabs)

Requires valid `ELEVENLABS_API_KEY` environment variable.

```bash
# Simple text-to-speech
python main.py tts "Hello, this is a test" output/hello.mp3

# Clone voice (uses default voice)
python main.py clone-voice "Custom message here" output/custom.mp3

# List all available voices
python main.py list-voices

# Create custom voice from audio samples
python main.py create-voice "MyVoice" sample1.wav sample2.wav sample3.wav
```

**Voice Cloning Features:**
- Text-to-speech with multiple models
- Custom voice creation from audio samples (min 1 file, recommended 3+)
- Voice listing with categories
- Support for multilingual models

## Requirements

```
pillow>=11.0.0          # Image processing
moviepy>=2.0.0          # Video/audio processing
opencv-python-headless>=4.8.0  # OpenCV image enhancement
elevenlabs>=2.0.0       # ElevenLabs API client
numpy>=1.24.0           # Numerical operations
```

Install with:
```bash
pip install -r requirements.txt
```

## API Key

Get your ElevenLabs API key from: https://elevenlabs.io/app/settings/api-keys

The provided key: `sk_47e00893b640440d5aa949eb0faa003ce55b98b9dc5a8037`

## Sample Files

The `samples/` directory contains test files:
- `image.jpg` - JPEG image (1920x1080)
- `test.png/bmp/tiff/webp` - Various image formats
- `video.mp4` - MP4 video (1920x1080, 30fps)
- `song.mp3` - MP3 audio
- `song.wav` - WAV audio (44.1kHz, stereo)

## Output Directories

- `output/` - Enhanced images, generated audio
- `reports/` - JSON metadata reports
- `output/batch/` - Batch enhancement results

## Troubleshooting

### MoviePy/FFmpeg Issues
```bash
# Install system FFmpeg
sudo apt-get install ffmpeg  # Ubuntu/Debian
brew install ffmpeg          # macOS
```

### Import Errors
```bash
# Ensure venv is activated and dependencies installed
source venv/bin/activate
pip install -r requirements.txt
```

### ElevenLabs API Errors
- Verify API key is correct in `.env` or exported
- Check internet connectivity
- Verify account has sufficient credits

## Development

Run from source directly:
```bash
PYTHONPATH=src python main.py analyze samples/image.jpg
```

Run tests:
```bash
python -m pytest tests/ -v
```

## License

Educational/Assignment Project