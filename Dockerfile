FROM nvidia/cuda:11.4.3-cudnn8-devel-ubuntu20.04

# expose
EXPOSE 8080

# set working directory
WORKDIR /app

# install pip and git
ENV DEBIAN_FRONTEND=noninteractive 
RUN apt-get update && apt-get install -y python3-pip git ffmpeg fluidsynth

# install poetry
RUN pip3 install --upgrade poetry

# add requirements
COPY ./pyproject.toml .
COPY ./poetry.lock .

# install requirements
RUN poetry install

# add source code
COPY . .

# run server
CMD poetry run python basic_pitch_demo/app.py