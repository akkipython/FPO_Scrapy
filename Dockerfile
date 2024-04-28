
FROM python:3.10

WORKDIR /app/zabuacrop

COPY zabuacrop/requirements.txt /app/zabuacrop

RUN pip install --no-cache-dir -r requirements.txt

COPY zabuacrop /app

