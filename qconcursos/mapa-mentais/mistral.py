import base64
import os
from mistralai import Mistral
from dotenv import load_dotenv

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

api_key = os.environ.get("MISTRAL_API_KEY")
if not api_key:
    raise EnvironmentError("A variável MISTRAL_API_KEY não está definida")

client = Mistral(api_key=api_key)

base64_image = encode_image("primeira.png")

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type": "image_url",
        "image_url": f"data:image/png;base64,{base64_image}"
    },
    include_image_base64=True
)

markdown = "\n\n".join([page.markdown for page in ocr_response.pages])

with open("ocr_output.txt", "w", encoding="utf-8") as f:
    f.write(markdown)
