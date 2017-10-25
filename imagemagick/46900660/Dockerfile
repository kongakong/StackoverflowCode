FROM ubuntu:16.04


RUN apt-get update --fix-missing 
RUN apt-get install -y libmagickwand-dev wget


WORKDIR '/src'
ENV IMAGEMAGICK_VERSION 6.9.9-19
RUN wget --no-check-certificate https://github.com/ImageMagick/ImageMagick/archive/${IMAGEMAGICK_VERSION}.tar.gz -O ${IMAGEMAGICK_VERSION}.tar.gz && \
    tar -zxvf ${IMAGEMAGICK_VERSION}.tar.gz && \
    cd ImageMagick-${IMAGEMAGICK_VERSION} && \
    ./configure && \
    make && \
    make install && \
    ldconfig /usr/local/lib

