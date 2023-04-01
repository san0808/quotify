from fastapi import APIRouter
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from fastapi.responses import StreamingResponse
import requests
router = APIRouter()

@router.post('/generate_image')
async def generate_image(prompt: str):
    # Generate the image bytes using Stable Diffusion or Dalle
    image_bytes = generate_image_using_stable_diffusion(prompt)
    
    # Return the image bytes as a streaming response
    return StreamingResponse(BytesIO(image_bytes), media_type="image/png")

def generate_image_using_stable_diffusion(prompt: str) -> bytes:
    # TODO: Implement function to generate image using Stable Diffusion or Dalle
    # Here's an example of how you might use the Unsplash API to get a random image:
    response = requests.get("https://api.unsplash.com/photos/random", headers={
        "Accept-Version": "v1",
        "Authorization": "Client-ID gG_ClSiPX9v9pEPonerXlUu28wrClQjOKYujnPkDoWo"
    })
    image_url = response.json()["urls"]["regular"]
    
    # Open the image from the URL and add the quote text
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content)).convert("RGBA")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", size=24)
    draw.text((50, 50), prompt, font=font, fill=(255, 255, 255, 255))
    
    # Save the image to a byte stream and return it
    output = BytesIO()
    image.save(output, format="PNG")
    return output.getvalue()



# from fastapi import APIRouter
# from PIL import Image, ImageDraw, ImageFont
# from dalle_mini import load_model, generate_images
# import requests
# from io import BytesIO

# router = APIRouter()

# # Load the DALL-E model
# model = load_model("dalle-mini")

# @router.post("/generate_image")
# async def generate_image(prompt: str):
#     # Generate the image using the DALL-E model
#     image = generate_images(
#         prompt=prompt,
#         model=model,
#         batch_size=1,
#         top_k=1,
#         temperature=1.0
#     )[0]

#     # Convert the image from a NumPy array to a PIL Image
#     image = Image.fromarray(image)

#     # Resize the image to a fixed size
#     image = image.resize((800, 600))

#     # Add the quote to the image using a specified font and color
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.truetype("arial.ttf", 50)
#     text_color = (255, 255, 255)
#     text_position = (50, 50)
#     draw.text(text_position, prompt, font=font, fill=text_color)

#     # Convert the PIL Image to a bytes object for streaming to the client
#     image_bytes = BytesIO()
#     image.save(image_bytes, format="JPEG")
#     image_bytes = image_bytes.getvalue()

#     # Return the image as a streaming response
#     return StreamingResponse(io.BytesIO(image_bytes), media_type="image/jpeg")
