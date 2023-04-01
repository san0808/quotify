from fastapi import FastAPI, HTTPException,Request
# from fastapi.responses import JSONResponse
# import logging
# import openai
# import requests
# from api.endpoints import generate_image, get_prompt
from api.endpoints.generate_image import router as generate_image_router

from api.endpoints.get_prompt import router as get_prompt_router
app = FastAPI()

app.include_router(generate_image_router)
app.include_router(get_prompt_router)

# @app.post("/get_prompt")
# async def get_prompt(quote: str):
#     # TODO: Implement function to generate a prompt from ChatGPT
#     prompt = generate_prompt_from_chatgpt(quote)
#     return {"prompt": prompt}

# @app.post("/generate_image")
# async def generate_image(prompt: str):
#     # TODO: Implement function to generate an image using Stable Diffusion or Dalle
#     image_url = generate_image_using_stable_diffusion(prompt)
#     return {"image_url": image_url}

# def generate_prompt_from_chatgpt(quote: str) -> str:
#     # Initialize OpenAI API
#     openai.api_key = "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"

#     # Generate prompt using OpenAI's GPT-3 model
#     prompt = "Generate a text description for the following quote: " + quote
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     prompt = response.choices[0].text.strip()
#     return prompt

# def generate_image_using_stable_diffusion(prompt: str) -> str:
#     # Generate image using Stable Diffusion or Dalle
#     # TODO: Implement function to generate image using Stable Diffusion or Dalle
#     # Here's an example of how you might use the Unsplash API to get a random image:
#     response = requests.get("https://api.unsplash.com/photos/random", headers={
#         "Accept-Version": "v1",
#         "Authorization": "Client-ID gG_ClSiPX9v9pEPonerXlUu28wrClQjOKYujnPkDoWo"
#     })
#     image_url = response.json()["urls"]["regular"]
#     return image_url

# logger = logging.getLogger("uvicorn")

# @app.exception_handler(HTTPException)
# async def http_exception_handler(request, exc):
#     logger.error(exc.detail)
#     return {"error": exc.detail}

# @app.exception_handler(Exception)
# async def exception_handler(request: Request, exc: Exception):
#     # TODO: Implement error handling logic here
#     error_message = f"An error occurred: {exc}"
#     return JSONResponse(status_code=500, content={"message": error_message})