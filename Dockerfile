FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install -y python3.9 python3-pip

WORKDIR /app

COPY web/dist ./web/dist
COPY proj ./proj
COPY app.py ./app.py

COPY requirements.txt /tmp/requirements.txt
RUN ["pip3", "install", "-i","https://pypi.tuna.tsinghua.edu.cn/simple","-r", "/tmp/requirements.txt"]

EXPOSE 5000

CMD [ "python3","app.py" ]