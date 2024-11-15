ARG FROM
FROM ${FROM}

MAINTAINER nutonomy.com

RUN apt-get update && apt-get install -y --no-install-recommends \
      curl \
      libsm6 \
      libxext6 \
      libxrender-dev \
      libgl1-mesa-glx \
      libglib2.0-0 \
      xvfb \
    && rm -rf /var/lib/apt/lists/*

RUN curl -OL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && bash ./Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda3 \
    && rm -f Miniconda3-latest-Linux-x86_64.sh

ENV PATH /opt/miniconda3/bin:$PATH

RUN conda update -n base -c defaults conda

RUN groupadd -g 1000 dev \
    && useradd -d /home/vod -u 1000 -g 1000 -m -s /bin/bash dev

USER dev

WORKDIR /vod-dev/prediction

ENV PYTHONPATH=/vod-dev/python-sdk

COPY setup/requirements.txt .

RUN bash -c "conda create -y -n vod python=3.7 \
    && source activate vod \
    && pip install --no-cache-dir -r /vod-dev/prediction/requirements.txt \
    && conda clean --yes --all"

VOLUME [ '/vod-dev/python-sdk', '/vod-dev/prediction', '/data/sets/vod', '/vod-dev/Documents' ]
