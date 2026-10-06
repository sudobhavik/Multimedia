import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import os


def enhance_image_opencv(input_path: str, output_path: str, enhancements: dict = None) -> dict:
    """
    Enhance image using OpenCV.
    
    Args:
        input_path: Path to input image
        output_path: Path to save enhanced image
        enhancements: Dict with enhancement options:
            - denoise: bool (default True)
            - sharpen: bool (default True)
            - contrast: float (default 1.2)
            - brightness: float (default 1.0)
            - saturation: float (default 1.1)
            - super_resolution: bool (default False)
            - upscale_factor: int (default 2)
    
    Returns:
        dict with status and details
    """
    try:
        img = cv2.imread(input_path)
        if img is None:
            return {"status": "error", "message": "Could not read image"}
        
        if enhancements is None:
            enhancements = {}
        
        # Denoising
        if enhancements.get("denoise", True):
            img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
        
        # Contrast and Brightness
        contrast = enhancements.get("contrast", 1.2)
        brightness = enhancements.get("brightness", 1.0)
        img = cv2.convertScaleAbs(img, alpha=contrast, beta=(brightness - 1.0) * 50)
        
        # Sharpening
        if enhancements.get("sharpen", True):
            kernel = np.array([[-1, -1, -1],
                              [-1,  9, -1],
                              [-1, -1, -1]])
            img = cv2.filter2D(img, -1, kernel)
        
        # Saturation adjustment (convert to HSV)
        saturation = enhancements.get("saturation", 1.1)
        if saturation != 1.0:
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            hsv = hsv.astype(np.float32)
            hsv[:, :, 1] = hsv[:, :, 1] * saturation
            hsv[:, :, 1] = np.clip(hsv[:, :, 1], 0, 255)
            hsv = hsv.astype(np.uint8)
            img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        
        # Super resolution / Upscaling
        if enhancements.get("super_resolution", False):
            scale = enhancements.get("upscale_factor", 2)
            try:
                sr = cv2.dnn_superres.DnnSuperResImpl_create()
                model_path = "EDSR_x2.pb"  # Would need to be downloaded
                if os.path.exists(model_path):
                    sr.readModel(model_path)
                    sr.setModel("edsr", scale)
                    img = sr.upsample(img)
                else:
                    # Fallback to simple resize
                    h, w = img.shape[:2]
                    img = cv2.resize(img, (w * scale, h * scale), interpolation=cv2.INTER_CUBIC)
            except Exception:
                h, w = img.shape[:2]
                scale = enhancements.get("upscale_factor", 2)
                img = cv2.resize(img, (w * scale, h * scale), interpolation=cv2.INTER_CUBIC)
        
        cv2.imwrite(output_path, img)
        
        return {
            "status": "success",
            "input_path": input_path,
            "output_path": output_path,
            "enhancements_applied": enhancements
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


def enhance_image_pil(input_path: str, output_path: str, enhancements: dict = None) -> dict:
    """
    Enhance image using PIL/Pillow.
    
    Args:
        input_path: Path to input image
        output_path: Path to save enhanced image
        enhancements: Dict with enhancement options:
            - contrast: float (default 1.2)
            - brightness: float (default 1.1)
            - sharpness: float (default 1.5)
            - color: float (default 1.1)
            - denoise: bool (default True)
    
    Returns:
        dict with status and details
    """
    try:
        img = Image.open(input_path)
        
        if enhancements is None:
            enhancements = {}
        
        # Contrast
        if "contrast" in enhancements:
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(enhancements["contrast"])
        
        # Brightness
        if "brightness" in enhancements:
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(enhancements["brightness"])
        
        # Sharpness
        if "sharpness" in enhancements:
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(enhancements["sharpness"])
        
        # Color/Saturation
        if "color" in enhancements:
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(enhancements["color"])
        
        # Denoise using filter
        if enhancements.get("denoise", True):
            img = img.filter(ImageFilter.MedianFilter(size=3))
        
        img.save(output_path)
        
        return {
            "status": "success",
            "input_path": input_path,
            "output_path": output_path,
            "enhancements_applied": enhancements
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


def enhance_image_auto(input_path: str, output_path: str, method: str = "pil") -> dict:
    """
    Auto-enhance image with sensible defaults.
    
    Args:
        input_path: Path to input image
        output_path: Path to save enhanced image
        method: "pil" or "opencv"
    
    Returns:
        dict with status and details
    """
    if method == "opencv":
        return enhance_image_opencv(input_path, output_path, {
            "denoise": True,
            "sharpen": True,
            "contrast": 1.3,
            "brightness": 1.1,
            "saturation": 1.15
        })
    else:
        return enhance_image_pil(input_path, output_path, {
            "contrast": 1.3,
            "brightness": 1.15,
            "sharpness": 2.0,
            "color": 1.15,
            "denoise": True
        })


def batch_enhance(input_dir: str, output_dir: str, method: str = "pil") -> dict:
    """Batch enhance all images in a directory."""
    os.makedirs(output_dir, exist_ok=True)
    
    results = []
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.tif', '.webp', '.bmp')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"enhanced_{filename}")
            result = enhance_image_auto(input_path, output_path, method)
            results.append(result)
    
    return {
        "status": "success",
        "processed": len(results),
        "results": results
    }