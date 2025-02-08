FROM python
 
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000


COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh


ENTRYPOINT ["/app/entrypoint.sh"]
