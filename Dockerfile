FROM python:3.10-slim

WORKDIR /trackerApp

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "trackerApp.py"]