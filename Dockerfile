FROM ubuntu:16.04
ADD . /code
WORKDIR /code

RUN \
  apt-get -y update && \
  apt-get install -y python3-pip python3-dev &&\
  cd /usr/local/bin &&\
  ln -s /usr/bin/python3 python &&\
  pip3 install --upgrade pip &&\
  apt-get -y install portaudio19-dev && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt
