import requests
from PIL import Image
from io import BytesIO

def download_image(url: str):
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        img = Image.open(BytesIO(resp.content)).convert("RGBA")
        local_path = "/tmp/input_image.png"
        img.save(local_path, "PNG")
        return local_path, img
    except:
        return None, None

def validate_bbox(img, bbox):
    width, height = img.size
    if 0 <= bbox.x_min < bbox.x_max <= width and 0 <= bbox.y_min < bbox.y_max <= height:
        return True
    return False
