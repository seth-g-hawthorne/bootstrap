#!/bin/bash
# Install useful utilities
#
pushd "${BASH_SOURCE[0]}" > /dev/null
  sudo apt-install jq

  ./install-kubebox.sh
  ./install-kubetail.sh
  ./install-kubectx.sh
  ./config-bash-autocomplete.sh

popd > /bin/bash