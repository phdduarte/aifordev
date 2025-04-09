# Processador de Mapas Mentais

Este projeto converte mapas mentais de imagens para formato JSON estruturado usando OCR e processamento de linguagem natural.

## Requisitos

- Python 3.8+
- Bibliotecas Python (instaladas automaticamente):
  - openai
  - python-dotenv
  - mistralai

## Configuração

1. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
   ```
   MISTRAL_API_KEY="sua_chave_mistral"
   OPENAI_API_KEY="sua_chave_openai"
   ```

2. Configure um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

## Uso

Execute o script `run.sh` para processar as imagens:

```bash
chmod +x run.sh  # Torne o script executável (apenas na primeira vez)
./run.sh
```

O processamento ocorre em duas etapas:
1. OCR: extração de texto da imagem usando a API Mistral
2. Estruturação: conversão do texto em JSON estruturado usando a API OpenAI

## Arquivos de Saída

- `ocr_output.txt`: Texto extraído da imagem
- `mapa_mental.json`: Mapa mental estruturado em formato JSON 
