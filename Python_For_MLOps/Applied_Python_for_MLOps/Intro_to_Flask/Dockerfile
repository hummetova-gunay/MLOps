FROM python:3.8

WORKDIR /webapp

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY webapp/ .

CMD ["python", "app.py"]
