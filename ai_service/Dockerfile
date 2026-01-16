# Usa uma imagem leve do Python
FROM python:3.8-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos necessários
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY log_analyzer.py .

# Cria as pastas que o script espera (mapeadas por volumes depois)
RUN mkdir -p /data /model

# Comando para rodar o script e manter o container vivo para análise
CMD ["python", "-u", "log_analyzer.py"]