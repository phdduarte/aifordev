import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a chave da API da OpenAI do arquivo .env
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("A variável OPENAI_API_KEY não está definida")

# Inicializa o cliente da OpenAI
client = OpenAI(api_key=api_key)

def ler_texto_ocr(caminho_arquivo):
    """Lê o conteúdo do arquivo de texto OCR."""
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        return arquivo.read()

def gerar_mapa_mental(texto_ocr):
    """Gera um mapa mental estruturado usando a API da OpenAI."""
    resposta = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system", 
                "content": "Você é um assistente especializado em criar mapas mentais estruturados em formato JSON."
            },
            {
                "role": "user", 
                "content": f"Baseado nas informações fornecidas, crie um mapa mental em formato JSON que organiza os conceitos de ortografia e acentuação gráfica:\n\n{texto_ocr}"
            }
        ],
        temperature=0.2,
    )
    
    return resposta.choices[0].message.content

def salvar_json(conteudo, caminho_arquivo):
    """Extrai e salva apenas o conteúdo JSON da resposta."""
    # Procura por conteúdo JSON entre ```json e ```
    inicio = conteudo.find("```json\n")
    fim = conteudo.find("```", inicio + 8)
    
    if inicio != -1 and fim != -1:
        json_puro = conteudo[inicio + 8:fim].strip()
    else:
        # Se não estiver no formato de bloco de código, tenta usar todo o conteúdo
        json_puro = conteudo
    
    try:
        # Verifica se o JSON é válido
        dados_json = json.loads(json_puro)
        
        # Salva o JSON formatado no arquivo
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados_json, arquivo, ensure_ascii=False, indent=2)
        
        return True
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        return False

def processar():
    """Função principal que coordena o processamento completo."""
    # Caminho do arquivo de texto OCR
    caminho_ocr = "ocr_output.txt"
    # Caminho para salvar o JSON resultante
    caminho_json = "mapa_mental.json"
    
    # Lê o texto OCR
    texto_ocr = ler_texto_ocr(caminho_ocr)
    
    # Gera o mapa mental
    conteudo_json = gerar_mapa_mental(texto_ocr)
    
    # Salva o JSON
    if salvar_json(conteudo_json, caminho_json):
        print(f"Mapa mental salvo com sucesso em {caminho_json}")
    else:
        print("Erro ao salvar o mapa mental.")

if __name__ == "__main__":
    processar() 
