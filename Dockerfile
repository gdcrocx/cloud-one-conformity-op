FROM registry.cto.ai/official_images/python:2-3.7-buster-slim

WORKDIR /ops

COPY --chown=ops:9999 requirements.txt .

RUN pip3 install -r requirements.txt

COPY --chown=ops:9999 . .

COPY --chown=ops:9999 cloudformation/ /tmp/cloudformation/