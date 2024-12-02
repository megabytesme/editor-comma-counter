FROM python:3.10-alpine

RUN apk add --no-cache curl gcc musl-dev bash

RUN pip install flask flask_cors

WORKDIR /app

COPY src/main.py /app/

EXPOSE 5000

CMD ["python3", "main.py"]
