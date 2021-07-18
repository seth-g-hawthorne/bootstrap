#!/bin/bash
#
pushd "$(dirname $0)" > /dev/null
  kubectl delete -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-rc6/aio/deploy/recommended.yaml
  kubectl delete -f dashboard-user.yaml
popd > /dev/null


