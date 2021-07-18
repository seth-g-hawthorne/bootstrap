#!/bin/bash
pushd "$(dirname $0)" > /dev/null
  kubectl apply -f deploy.yaml
popd > /dev/null


