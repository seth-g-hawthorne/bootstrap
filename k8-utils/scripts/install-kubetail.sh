#!/bin/bash
# Install the kubetail utility
#
pushd "${BASH_SOURCE[0]}" > /dev/null
  if [ ! -e kubetail ]; then
    wget -O kubetail https://raw.githubusercontent.com/johanhaleby/kubetail/master/kubetail
    chmod +x kubetail
  fi
popd > /dev/null