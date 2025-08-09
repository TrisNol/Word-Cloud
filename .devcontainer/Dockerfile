FROM mcr.microsoft.com/devcontainers/python:3.12
# Install common tools
RUN apt-get update && apt-get -y install apt-utils curl git gnupg2 zsh

# Install further packages required for OpenCVs
RUN apt-get update && apt-get -y install ffmpeg libsm6 libxext6

# Install Node 22 for the frontend
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
RUN apt-get install -y nodejs
    
# Install Docker for build and test processes
RUN curl -fsSL https://get.docker.com | sh

# Install & configure oh-my-zsh
ADD .zshrc $HOME/.zshrc