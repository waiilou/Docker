FROM python:3.12.0-alpine

WORKDIR .

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 6090

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6090"]