
from fastapi import APIRouter, HTTPException
from .models import InputPayload, SuccessResponse, ErrorResponse
from .utils import download_image, validate_bbox
from .processing import remove_background
from .storage import upload_to_s3
import uuid

router = APIRouter()

@router.post("/remove_background", response_model=SuccessResponse, responses={400: {"model": ErrorResponse}, 500: {"model": ErrorResponse}})
async def remove_background_api(payload: InputPayload):
    image_path, img = download_image(str(payload.image_url))
    if img is None:
        raise HTTPException(status_code=400, detail="Invalid image URL or image not accessible.")
    
    if not validate_bbox(img, payload.bounding_box):
        raise HTTPException(status_code=400, detail="Bounding box is invalid or out of image bounds.")
    
    try:
        processed_img_path = remove_background(image_path, payload.bounding_box)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")
    
    file_name = f"processed_{uuid.uuid4()}.png"
    s3_url = upload_to_s3(processed_img_path, file_name)

    return SuccessResponse(
        original_image_url=str(payload.image_url),
        processed_image_url=s3_url
    )
