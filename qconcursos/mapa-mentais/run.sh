#!/bin/bash

# Ativar ambiente virtual
source venv/bin/activate

# Verificar se os pacotes necessários estão instalados
pip install -r requirements.txt

# Executar o script OCR com Mistral
echo "Executando processamento OCR..."
python mistral.py 

# Executar o processador OpenAI para gerar JSON
echo "Gerando mapa mental em JSON com OpenAI..."
python openai_processor.py

echo "Processamento concluído! Verifique o arquivo mapa_mental.json" 
