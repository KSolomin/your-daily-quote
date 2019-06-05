FROM python:3.6.8-alpine
RUN apk update \
    && mkdir -p /var/www/logs
WORKDIR /var/www
# Not obvious, but the following command copies source code into WORKDIR
COPY . .
RUN pip install -r source/requirements.txt
EXPOSE 5000
CMD ["python", "source/main.py"]
