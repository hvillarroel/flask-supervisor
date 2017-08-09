FROM python:3.6

RUN pip install pip --upgrade

WORKDIR /application/app

COPY setup.py setup.py
COPY requirements.txt requirements.txt
COPY config.ini.template config.ini

RUN ls -l && pwd

RUN pip install -r requirements.txt

ENV LC_ALL=C.UTF-8
ENV FLASK_APP=app/server.py
ENV FLASK_DEBUG=1
CMD ["flask", "run", "-h", "0.0.0.0"]
