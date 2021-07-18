#!/bin/bash
pushd "$(dirname $0)" > /dev/null
  kubectl delete -f deploy.yaml
popd > /dev/null
