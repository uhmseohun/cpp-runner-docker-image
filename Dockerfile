FROM ubuntu:16.04

LABEL maintainer Seohun Uhm

# Install GCC, Python3
RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y g++

COPY run.py /src/run.py

CMD [ "mkdir", "/src" ]
WORKDIR /src

# Build Context and Source Code File Should Be Copied Into /src

ENTRYPOINT [ "python3", "run.py" ]
