## Referência para criação da imagem multi-staged: https://pythonspeed.com/articles/multi-stage-docker-python/

FROM python:3.7-buster AS compile-image

COPY app/requirements.txt /app/requirements.txt

RUN apt update && apt install -y gettext libpq-dev python-dev libldap2-dev libsasl2-dev python-ldap git
RUN pip3 install --user -r /app

COPY app/ /app 

WORKDIR /app

ENTRYPOINT ["python","/app/app.py"]
