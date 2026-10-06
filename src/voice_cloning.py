import os
from elevenlabs.client import ElevenLabs
from elevenlabs import play, save


def clone_voice(api_key: str, text: str, voice_id: str = None, output_path: str = "output_audio.mp3", model_id: str = "eleven_multilingual_v2") -> dict:
    """
    Clone voice using ElevenLabs API.
    
    Args:
        api_key: ElevenLabs API key
        text: Text to synthesize
        voice_id: Voice ID to use (if None, uses default)
        output_path: Path to save the generated audio
        model_id: Model to use for synthesis
    
    Returns:
        dict with status and output path
    """
    try:
        client = ElevenLabs(api_key=api_key)
        
        if voice_id is None:
            voices = client.voices.get_all()
            if voices.voices:
                voice_id = voices.voices[0].voice_id
            else:
                return {"status": "error", "message": "No voices available"}
        
        audio = client.text_to_speech.convert(
            voice_id=voice_id,
            text=text,
            model_id=model_id,
        )
        
        save(audio, output_path)
        
        return {
            "status": "success",
            "output_path": output_path,
            "voice_id": voice_id,
            "model_id": model_id,
            "text": text
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


def create_voice_clone(api_key: str, name: str, audio_files: list, description: str = "") -> dict:
    """
    Create a custom voice clone from audio samples.
    
    Args:
        api_key: ElevenLabs API key
        name: Name for the new voice
        audio_files: List of paths to audio files for training
        description: Description of the voice
    
    Returns:
        dict with status and voice_id
    """
    try:
        client = ElevenLabs(api_key=api_key)
        
        voice = client.voices.add(
            name=name,
            files=audio_files,
            description=description
        )
        
        return {
            "status": "success",
            "voice_id": voice.voice_id,
            "name": name
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


def list_voices(api_key: str) -> dict:
    """List all available voices."""
    try:
        client = ElevenLabs(api_key=api_key)
        voices = client.voices.get_all()
        
        voice_list = []
        for v in voices.voices:
            voice_list.append({
                "voice_id": v.voice_id,
                "name": v.name,
                "category": v.category,
                "description": v.description
            })
        
        return {"status": "success", "voices": voice_list}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def text_to_speech(api_key: str, text: str, voice_id: str = None, output_path: str = "output.mp3") -> dict:
    """
    Simple text-to-speech using ElevenLabs.
    """
    return clone_voice(api_key, text, voice_id, output_path)