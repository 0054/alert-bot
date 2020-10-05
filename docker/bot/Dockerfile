FROM python:alpine3.8

COPY ./bot /bot
WORKDIR /bot
RUN apk add --no-cache build-base libffi-dev openssl-dev
RUN pip install -r requirements.txt

CMD ["python", "./bot.py"]
