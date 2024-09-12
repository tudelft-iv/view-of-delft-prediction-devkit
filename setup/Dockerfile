FROM continuumio/miniconda3:4.6.14
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libsm6 \
        libxext6 \
        libxrender-dev \
        libgl1-mesa-glx \
        libglib2.0-0 \
        xvfb && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /vod-dev
# create conda vod env
ARG PYTHON_VERSION
RUN bash -c "conda create -y -n vod python=${PYTHON_VERSION} \
    && source activate vod \
    && conda clean --yes --all"

COPY setup/requirements.txt .
COPY setup/requirements/ requirements/
# Install Python dependencies inside of the Docker image via pip & Conda.
# pycocotools installed from conda-forge
RUN bash -c "source activate vod \
    && find . -name "\\*.txt" -exec sed -i -e '/pycocotools/d' {} \; \
    && pip install --no-cache -r /vod-dev/requirements.txt \
    && conda config --append channels conda-forge \
    && conda install --yes pycocotools \
    && conda clean --yes --all"