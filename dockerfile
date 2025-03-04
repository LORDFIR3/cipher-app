FROM python:3.9-slim

WORKDIR /app

RUN python -m ensurepip --upgrade

RUN pip --version

RUN pip install flask

RUN ls -l

COPY . .

EXPOSE 5000

ENV FLASK_ENV=production

CMD ["python3", "main.py"]
