#!/bin/bash
# Run on master node to install the Container Network Interface provider (Flanel)
#
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/3f7d3e6c24f641e7ff557ebcea1136fdf4b1b6a1/Documentation/kube-flannel.yml
