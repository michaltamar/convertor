# Convertor

## Build Docker Image

```bash
docker build -t convertor .
## הפעלת התמונה
להפעלת התמונה עם טעינת התיקיות והגדרת שם PDF מותאם אישית:
```bash
docker run -v $(pwd)/images:/app/images -v $(pwd)/output:/app/output -e PDF_NAME=my_pdf_name.pdf mydockerimage
