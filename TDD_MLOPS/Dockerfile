FROM linuxmintd/mint20-amd64:latest

WORKDIR /tdd

RUN apt update
RUN apt install -y python3 
RUN apt install -y build-essential checkinstall
RUN apt install -y libreadline-gplv2-dev
RUN apt install -y libncursesw5-dev
RUN apt install -y libssl-dev
RUN apt install -y libsqlite3-dev
RUN apt update
RUN apt install -y tk-dev
RUN apt install -y libgdbm-dev
RUN apt install -y libc6-dev
RUN apt install -y libbz2-dev 
RUN apt install -y git
RUN apt install -y python3-setuptools
RUN apt install -y python3-pip
RUN apt remove python-is-python2
RUN apt install -y python-is-python3

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN rm -r requirements.txt

EXPOSE 22

