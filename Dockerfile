FROM debian:latest

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update && apt-get -y upgrade \
    && apt-get -y --no-install-recommends install \
        cpanminus \
        gcc \
        libc6-dev \
        linux-libc-dev \
        make \
        python3-pip \
        python3-setuptools \
    && rm -r /var/lib/apt/lists/* \
    && export MAKEFLAGS=-j$(nproc) \
    && cpanm --notest Perl::Critic \
    && rm -r /root/.cpanm \
    && pip3 install flake8 flake8-bugbear \
    && rm -r /root/.cache/pip \
    && mkdir /work

WORKDIR /work
