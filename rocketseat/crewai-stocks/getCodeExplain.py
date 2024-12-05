from openai import OpenAI
import os
import json

load_dotenv()

client = OpenAI(
  organization=os.getenv('OPENAI_ORG'),
  project=os.getenv('OPENAI_PROJECT'),
  api_key=os.getenv('Q_API_KEY')
)

# stream = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[{"role": "user", "content": "Say this is a test"}],
#     stream=True,
# )

# Listar modelos e convertê-los em um formato serializável
# models_data = [model.to_dict() for model in client.models.list().data]

# Serializar para JSON
# formatted_data = json.dumps(models_data, indent=4)
# print(formatted_data)

codigo_str = """
from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(
  organization=os.getenv('OPENAI_ORG'),
  project=os.getenv('OPENAI_PROJECT'),
  api_key=os.getenv('Q_API_KEY')
)

stream = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Você irá receber um código e gostaria de uma explicação detalhada sobre o funcionamento do código."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ],
  stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
"""


stream = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Você irá receber um código e gostaria de uma explicação detalhada sobre o funcionamento do código."},
    {"role": "user", "content": codigo_str}
    # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    # {"role": "user", "content": "Where was it played?"}
  ],
  stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print((chunk.choices[0].delta.content).encode('-uft-8'), end="")
