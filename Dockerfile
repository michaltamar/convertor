FROM python:3.9-slim

# תיקון בעיות תעודות (אם צריך)
RUN apt update && apt install -y curl
RUN curl -sL https://netfree.link/dl/unix-ca.sh | sh
RUN pip config set global.cert /usr/lib/ssl/certs/ca-certificates.crt

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY convert_image_to_pdf.py .

ENTRYPOINT ["python", "convert_image_to_pdf.py"]
