FROM python:3.12
WORKDIR /app

RUN pip install gunicorn==22.0.0

COPY requirements/requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "catshare_backend.wsgi"]
