FROM python:3.12-slim

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 libgl1-mesa-glx  -y

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 3000

CMD [ "python", "./app.py" ]