from fastapi import FastAPI, HTTPException
import openai
from fastapi import APIRouter
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

router = APIRouter()

def generate_prompt_from_chatgpt(quote: str) -> str:
    # Initialize OpenAI API
    openai.api_key = openai_api_key

    # Generate prompt using OpenAI's GPT-3 model
    prompt = "Generate a text description for the following quote: " + quote
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    prompt = response.choices[0].text.strip()
    return prompt

@router.post("/get_prompt")
async def get_prompt(quote: str):
    try:
        # Generate a prompt from ChatGPT
        prompt = generate_prompt_from_chatgpt(quote)
        return {"prompt": prompt}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
