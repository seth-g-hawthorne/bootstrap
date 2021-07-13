#!/bin/bash
# Install Docker
# Ref: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
#
pushd "${BASH_SOURCE[0]}" > /dev/null
  ../../docker/install-ubuntu.sh 

  #systemd cgroup driver is prefered
  if [ ! -e /etc/docker/daemon.json ]; then
    cat <<EOT >> /etc/docker/daemon.json
    {
      "exec-opts": ["native.cgroupdriver=systemd"]
    }
EOT
  fi

popd > /dev/null