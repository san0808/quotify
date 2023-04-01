from pydantic import BaseModel

class Prompt(BaseModel):
    quote: str
    image_size: str = "1024x1024"
    font_family: str = "Arial"
    font_color: str = "#000000"
    background_color: str = "#FFFFFF"
