FROM python:3.11.0-slim
 
WORKDIR /app

COPY . /app

EXPOSE 8000

RUN pip install -r requirements.txt
 
CMD ["uvicorn", "main:app", "--reload"]
