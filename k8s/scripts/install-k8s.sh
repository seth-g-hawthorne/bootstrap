#!/bin/bash
# Install kubernetes on ubuntu
# Ref: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
#
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add
sudo apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
sudo apt-get update

sudo apt-get install kubeadm kubelet kubectl
# Disable updates
sudo apt-mark hold kubeadm kubelet kubectl
kubeadm version

