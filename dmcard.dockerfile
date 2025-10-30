# Stage 1: Build
FROM python:3.13-slim as builder
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt update && apt install -y --no-install-recommends gcc
WORKDIR /build
COPY requirements.txt .
#Instalação das dependências em uma pasta específica
RUN python -m venv /opt/venv && . /opt/venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.13-slim
# Labels informativos
LABEL maintainer="Danwiilo Ltda"
LABEL license="MIT License"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY --from=builder /opt/venv ./opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# Copia apenas os arquivos necessários
COPY ./api ./api
COPY ./core ./core
COPY ./models ./models
COPY ./schemas ./schemas
COPY ./main.py .
COPY ./create_tables.py .

EXPOSE 8000
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]