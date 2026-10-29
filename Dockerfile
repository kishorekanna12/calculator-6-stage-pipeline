FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

CMD ["python", "-c", "import time; print('Calculator Service Online'); [time.sleep(3600) for _ in iter(int, 1)]"]
