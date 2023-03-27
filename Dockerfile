FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY classes classes
COPY data data
COPY templates templates
COPY *.py ./

CMD  python wsgi.py