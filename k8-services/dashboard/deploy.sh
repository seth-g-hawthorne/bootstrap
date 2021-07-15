#!/bin/bash
#
pushd "${BASH_SOURCE[0]}" > /dev/null
  kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-rc6/aio/deploy/recommended.yaml
  kubectl apply -f dashboard-user.yaml
popd > /dev/null
