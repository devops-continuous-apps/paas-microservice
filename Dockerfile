FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

ENV FLASK_APP=src/main.py

CMD ["pipenv", "run", "flask", "run", "-h", "0.0.0.0", "-p", "3000"]
