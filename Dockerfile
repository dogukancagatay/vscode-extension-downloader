FROM python:3.9-alpine
LABEL org.opencontainers.image.authors="Dogukan Cagatay <dcagatay@gmail.com>"

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait

RUN pip install -U pip && \
    pip install wheel

WORKDIR /app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./

ENV REMOTE_DRIVER_URL "http://selenium:4444/wd/hub"
ENV WAIT_HOSTS "selenium:4444"
ENV WAIT_AFTER "3"
ENV WAIT_LOGGER_LEVEL "info"

CMD sh -xc '/wait && python main.py'
