#!/usr/bin/env python
import pytesseract
from PIL import Image
from openai import OpenAI
import os
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang="por", config="--psm 6")
    return text

image_path = "primeira.png"
extracted_text = extract_text_from_image(image_path)

with open("ocr_output.txt", "w", encoding="utf-8") as file:
    file.write(extracted_text)


def generate_mindmap(info_text):
    messages = [
        {
            "role": "system",
            "content": "Você é um especialista em criar mapas mentais em formato JSON com base em informações extraídas de imagens."
        },
        {
            "role": "user",
            "content": f"Crie um mapa mental em formato JSON com base nas seguintes informações extraídas de uma imagem: {info_text}"
        }
    ]
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.8,
        top_p=0.75,
        max_tokens=1500,
        messages=messages,
    )
    mindmap_json = response.choices[0].message.content
    return mindmap_json

mindmap = generate_mindmap(extracted_text)
print(mindmap)
