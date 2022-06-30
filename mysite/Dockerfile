FROM python:3.8
WORKDIR /code
ADD . /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh