FROM python:3.12-bookworm

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install watchdog

COPY . .

CMD ["watchmedo", "auto-restart", "--directory=.", "--pattern=*.py", "--recursive", "python", "main.py"]
