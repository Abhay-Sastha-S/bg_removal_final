from pydantic import BaseModel, HttpUrl

class BoundingBox(BaseModel):
    x_min: int
    y_min: int
    x_max: int
    y_max: int

class InputPayload(BaseModel):
    image_url: HttpUrl
    bounding_box: BoundingBox

class SuccessResponse(BaseModel):
    original_image_url: str
    processed_image_url: str

class ErrorResponse(BaseModel):
    error: str
