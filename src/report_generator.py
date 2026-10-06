class ReportGenerator:
    @staticmethod
    def generate_image_report(metadata: dict) -> str:
        lines = []
        lines.append("=" * 34)
        lines.append("IMAGE METADATA REPORT")
        lines.append("=" * 34)
        lines.append("")
        lines.append(f"File Name       : {metadata['file_name']}")
        lines.append(f"File Size       : {metadata['file_size']} bytes")
        lines.append(f"File Format     : {metadata['file_format']}")
        lines.append(f"Width           : {metadata['width']}")
        lines.append(f"Height          : {metadata['height']}")
        lines.append("Resolution      : N/A")
        lines.append(f"Color Mode      : {metadata['color_mode']}")
        lines.append("")
        lines.append("EXIF Metadata")
        lines.append("-" * 33)
        exif = metadata.get("exif", {})
        if exif:
            for key, value in exif.items():
                lines.append(f"{key}           : {value}")
        else:
            lines.append("No EXIF data found")
        lines.append("")
        return "\n".join(lines)

    @staticmethod
    def generate_video_report(metadata: dict) -> str:
        lines = []
        lines.append("=" * 34)
        lines.append("VIDEO METADATA REPORT")
        lines.append("=" * 34)
        lines.append("")
        lines.append(f"File Name       : {metadata['file_name']}")
        lines.append(f"File Size       : {metadata['file_size']} bytes")
        lines.append(f"Container       : {metadata['container']}")
        lines.append(f"Duration        : {metadata['duration']} seconds")
        lines.append("")
        lines.append("VIDEO")
        lines.append("-" * 33)
        lines.append(f"Resolution      : {metadata['resolution']}")
        lines.append(f"Frame Rate      : {metadata['frame_rate']}")
        lines.append(f"Bit Rate        : {metadata['bit_rate']}")
        lines.append(f"Codec           : {metadata['codec']}")
        lines.append("")
        lines.append("AUDIO")
        lines.append("-" * 33)
        lines.append(f"Codec           : {metadata['audio_codec']}")
        lines.append(f"Channels        : {metadata['audio_channels']}")
        lines.append(f"Sampling Rate   : {metadata['audio_sampling_rate']}")
        lines.append(f"Bit Rate        : {metadata['audio_bitrate']}")
        lines.append("")
        lines.append("METADATA")
        lines.append("-" * 33)
        lines.append("...")
        lines.append("")
        return "\n".join(lines)

    @staticmethod
    def generate_audio_report(metadata: dict) -> str:
        lines = []
        lines.append("=" * 34)
        lines.append("AUDIO METADATA REPORT")
        lines.append("=" * 34)
        lines.append("")
        lines.append(f"File Name       : {metadata['file_name']}")
        lines.append(f"File Size       : {metadata['file_size']} bytes")
        lines.append(f"Duration        : {metadata['duration']} seconds")
        lines.append("")
        lines.append("AUDIO")
        lines.append("-" * 33)
        lines.append(f"Codec           : {metadata['codec']}")
        lines.append(f"Channels        : {metadata['channels']}")
        lines.append(f"Sampling Rate   : {metadata['sampling_rate']}")
        lines.append(f"Bit Rate        : {metadata['bitrate']}")
        lines.append("")
        lines.append("METADATA")
        lines.append("-" * 33)
        lines.append("...")
        lines.append("")
        return "\n".join(lines)

    @staticmethod
    def generate_report(metadata: dict) -> str:
        file_type = metadata.get("file_type", "").lower()
        width = metadata.get("width")
        height = metadata.get("height")
        duration = metadata.get("duration")
        codec = metadata.get("codec")
        if file_type.startswith("image") or (file_type == "" and width and height):
            return ReportGenerator.generate_image_report(metadata)
        elif file_type.startswith("video"):
            return ReportGenerator.generate_video_report(metadata)
        elif file_type.startswith("audio") or (file_type == "" and codec):
            return ReportGenerator.generate_audio_report(metadata)
        return "Unknown file type"