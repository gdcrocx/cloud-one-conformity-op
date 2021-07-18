FROM registry.cto.ai/official_images/python:2-3.7-buster-slim

WORKDIR /ops

ADD --chown=ops:9999 requirements.txt .

RUN pip3 install -r requirements.txt

ADD --chown=ops:9999 . .

RUN chown -R ops:9999 .