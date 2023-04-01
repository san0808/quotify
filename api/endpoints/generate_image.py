import requests
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()  # load environment variables from .env file

API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")

router = APIRouter()

class GenerateImageRequest(BaseModel):
    prompt: str

class GenerateImageResponse(BaseModel):
    image_url: str

@router.post("/generate-image", response_model=GenerateImageResponse)
async def generate_image(request: GenerateImageRequest):
    # Generate image using Stable Diffusion API
    try:
        response = requests.post(
            "https://api.replicate.ai/v1/model/stability-ai/stable-diffusion/generate",
            json={
                "prompt": request.prompt,
                "num_images": 1,
                "size": 512
            },
            headers = {
                "Authorization": f"Bearer {API_TOKEN}",
                "Content-Type": "application/json"
            }
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Failed to generate image") from e

    try:
        # Extract image URL from the response
        image_url = response.json()["result"][0]["path"]
        return GenerateImageResponse(image_url=image_url)
    except (KeyError, IndexError):
        raise HTTPException(status_code=500, detail="Failed to extract image URL from response")
