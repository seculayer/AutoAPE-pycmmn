FROM seculayer/python:3.7-cuda11.2 as builder
MAINTAINER jinkim "jinkim@seculayer.com"

ARG app="/opt/app"

RUN sudo apt-get update -y
RUN sudo apt-get install -y build-essential cmake git pkg-config libgtk-3-dev \
        libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
        libxvidcore-dev libx264-dev libjpeg-dev libpng-dev libtiff-dev \
        gfortran openexr libatlas-base-dev \
        libtbb2 libtbb-dev libdc1394-22-dev

RUN mkdir -p $app
WORKDIR $app

COPY ./requirements.txt ./requirements.txt
RUN pip3.7 install --upgrade pip setuptools wheel
RUN pip3.7 install -r ./requirements.txt -t $app/lib

COPY ./pycmmn ./pycmmn
COPY ./setup.py ./setup.py

RUN pip3.7 install wheel
RUN python3.7 setup.py bdist_wheel

FROM seculayer/python:3.7-cuda11.2 as app
ARG app="/opt/app"

RUN mkdir -p /eyeCloudAI/app/ape/pycmmn \
    && mkdir -p /eyeCloudAI/data/processing/ape/models

RUN groupadd -g 1000 aiuser
RUN useradd -r -u 1000 -g aiuser aiuser
RUN chown -R aiuser:aiuser /eyeCloudAI

USER aiuser

WORKDIR /eyeCloudAI/app/ape/pycmmn

COPY --from=builder --chown=aiuser:aiuser "$app/lib" /eyeCloudAI/app/ape/pycmmn/lib/

COPY --from=builder --chown=aiuser:aiuser "$app/dist/pycmmn-1.0.0-py3-none-any.whl" /eyeCloudAI/app/ape/pycmmn/

RUN pip3.7 install /eyeCloudAI/app/ape/pycmmn/pycmmn-1.0.0-py3-none-any.whl --no-dependencies  \
    -t /eyeCloudAI/app/ape/pycmmn \
    && rm /eyeCloudAI/app/ape/pycmmn/pycmmn-1.0.0-py3-none-any.whl

ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8

CMD []
