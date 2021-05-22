FROM python:3.8
MAINTAINER "nhvduy@gmail.com"
ENV MEMCACHED_SERVER, MEMCACHED_PORT
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python" ] 
CMD [ "api.py" ]