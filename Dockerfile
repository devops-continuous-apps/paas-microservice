FROM public.ecr.aws/docker/library/python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV FLASK_APP=src/main.py

# Setup New Relic
ENV NEW_RELIC_APP_NAME="paas-microservice"
ENV NEW_RELIC_LOG=stdout
ENV NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
ENV NEW_RELIC_LOG_LEVEL=info

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "3000"]

ENTRYPOINT ["newrelic-admin", "run-program"]
