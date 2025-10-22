FROM python:3.13

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /src

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .


