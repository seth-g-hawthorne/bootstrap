#!/bin/bash
# Initialize a Kubernetes worker node 
#
pushd "${BASH_SOURCE[0]}" > /dev/null
  ./init-ubuntu-node.sh
  echo "Copy and run the join-cluster.sh script from the master node"
popd