#!/bin/bash
# Install kubernetes on ubuntu
# Ref: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
#
pushd "${BASH_SOURCE[0]}" > /dev/null
  ./install-docker.sh
  ./config-ubuntu.sh
  ./install-k8s.sh
popd 
