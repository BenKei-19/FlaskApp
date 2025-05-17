
FROM python:3.10-slim


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 3000


CMD ["python", "app.py"]
