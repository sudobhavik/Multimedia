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
