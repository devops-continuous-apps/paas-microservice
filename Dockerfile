FROM public.ecr.aws/docker/library/python:3.11

WORKDIR /app

COPY . .

RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

ENV FLASK_APP=src/main.py

CMD ["pipenv", "run", "flask", "run", "-h", "0.0.0.0", "-p", "3000"]
