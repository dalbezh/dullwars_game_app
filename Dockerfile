FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY classes classes
COPY data data
COPY templates templates
COPY *.py .

CMD python -m gunicorn app:app -b 0.0.0.0:8080 -w 4