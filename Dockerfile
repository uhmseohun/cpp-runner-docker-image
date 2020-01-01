FROM ubuntu:16.04

LABEL maintainer Seohun Uhm

# Install GCC, Python3
RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y g++

COPY run.py /src/run.py

# build-context.json and User Source Code Should Be Copied Into Conatiner (-v option)

CMD [ "mkdir", "/src" ]

# TEMP
COPY build-context.json /src/build-context.json
COPY 6a9cde-91c4df.cpp /src/6a9cde-91c4df.cpp

WORKDIR /src

ENTRYPOINT [ "python3", "run.py" ]
