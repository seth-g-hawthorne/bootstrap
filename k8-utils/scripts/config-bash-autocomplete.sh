#!/bin/bash
# Configure bash autocompletion for kubectl
# # Ref: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
#
if [ $(type -t _init_completion) != "function" ]; then
  echo "source /usr/share/bash-completion/bash_completion" >> ~/.bashrc
fi
if [ ! -e /etc/bash_completion.d/kubectl ]; then 
  kubectl completion bash > ~/kubectl_completion
  sudo mv ~/kubectl_completion /etc/bash_completion.d/kubectl
fi

