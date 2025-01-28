FROM python
 
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["sh", "-c", "python create_tables.py && uvicorn main:app --host 0.0.0.0 --port 80"]
