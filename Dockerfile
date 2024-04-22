FROM locustio/locust
WORKDIR /locust
COPY locustfile.py .
