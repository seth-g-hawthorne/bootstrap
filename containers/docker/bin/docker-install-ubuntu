#!/bin/bash
# Install Docker CE on Ubuntu
# Ref: https://docs.docker.com/engine/install/ubuntu/
#
DOCKER_VERSION=${DOCKER_VERSION:="stable"}
DOCKER_KEYRING="/usr/share/keyrings/docker-archive-keyring.gpg"

sudo apt-get update 
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o ${DOCKER_KEYRING}
echo \
  "deb [arch=amd64 signed-by=${DOCKER_KEYRING}] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) ${DOCKER_VERSION}" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null


sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

sudo groupadd docker
sudo usermod -aG docker ${USER}
echo "You must logout and back in to use Docker as a non-root user"
