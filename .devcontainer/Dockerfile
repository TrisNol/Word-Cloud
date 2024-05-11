FROM ubuntu:24.04
# Install common tools
RUN apt-get update && apt-get -y install apt-utils curl git gnupg2 zsh

# Install Python 3.12 for the backend
RUN apt-get update && apt-get -y install software-properties-common python3-launchpadlib python3-pip
RUN apt-get update && apt-get -y install python3.12 python3.12-dev python3.12-venv python-is-python3
RUN export PATH="$HOME/.local/bin:$PATH"

# Install further packages required for OpenCV
RUN apt-get update && apt-get -y install ffmpeg libsm6 libxext6

# Install Node 22 for the frontend
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
RUN apt-get install -y nodejs
    
# Install Docker for build and test processes
RUN echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian bookworm stable" | \
    tee /etc/apt/sources.list.d/docker.list
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | \
    gpg --dearmor -o /etc/apt/keyrings/docker.gpg
RUN apt update && apt -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Install & configure oh-my-zsh
ADD .zshrc $HOME/.zshrc
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"