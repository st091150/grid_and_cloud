FROM python:3.10

ENV FLASK_APP=app.py

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . .

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
