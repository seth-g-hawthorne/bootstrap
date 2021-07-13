#!/bin/bash
# Install a Kubernetes Master node on Ubuntu
#
pushd "${BASH_SOURCE[0]}" > /dev/null
  ./init-ubuntu-node.sh

  TEMPFILE=$(mktemp)
  sudo kubeadm init --pod-network-cidr=10.244.0.0/16  > ${TEMPFILE}
  echo "sudo \\" >> join-cluster.sh
  grep -A 1 "kubeadm join" $TEMPFILE >> join-cluster.sh
  chmod +x join-cluster.sh
  cat $TEMPFILE
  rm $TEMPFILE

  ./init-kubectl.sh
  ./install-cni.sh
  ../k8-utils/scripts/install-utils.sh
popd > /dev/null