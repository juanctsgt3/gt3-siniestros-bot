FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY bot_gt3_siniestros.py bot_gt3_siniestros.py

CMD ["python", "bot_gt3_siniestros.py"]
