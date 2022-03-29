FROM python:3.10-alpine

WORKDIR /app

RUN apk add --update-cache gcc libc-dev libffi-dev \
    && rm -rf /var/cache/apk/*

COPY requirements.txt .
RUN pip install -U pip \
    && pip install -r requirements.txt

COPY . .

ENV FLASK_ENV=production

ENTRYPOINT [ "python", "-m", "flask", "run" ]
