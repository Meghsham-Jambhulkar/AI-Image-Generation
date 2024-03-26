import torch
from diffusers import StableDiffusionPipeline

from dotenv import load_dotenv, find_dotenv
import os
from PIL import Image
import io

load_dotenv(find_dotenv())
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")


def generate_images(text_prompt: str) ->list:
    import requests

    API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}
    payload = {
        "inputs": text_prompt,
        "num_inference_steps":999,
        "width": 1080,
        "height": 720,
        "enhance_prompt": "yes",
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    image_bytes =  response.content

    img = Image.open(io.BytesIO(image_bytes))
    return img


#EXAMPLE PROMPT
# ultra realistic close up portrait beautiful galaxy in beautiful universe,most beautiful light blue nebula,  hyper detail, cinematic lighting, magic neon, dark red city, Canon EOS R3, f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame, 8K