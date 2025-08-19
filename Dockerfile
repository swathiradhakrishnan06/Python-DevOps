FROM python:3.13-slim

RUN mkdir -p /app
COPY . main.py /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN python3 -m textblob.download_corpora
EXPOSE 8080
CMD ["python", "main.py"]
