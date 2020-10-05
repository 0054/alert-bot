FROM python:alpine3.8

COPY ./receiver /receiver
WORKDIR /receiver
RUN apk add --no-cache build-base libffi-dev openssl-dev
RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["python", "./app.py"]
