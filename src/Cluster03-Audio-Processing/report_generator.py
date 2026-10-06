class ReportGenerator:
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
