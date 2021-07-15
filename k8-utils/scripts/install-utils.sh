#!/bin/bash
# Install useful utilities
#
pushd "${BASH_SOURCE[0]}" > /dev/null
  ./install-jq.sh
  ./install-httpie.sh

  ./install-kubebox.sh
  ./install-kubetail.sh
  ./install-kubectx.sh
  ./config-bash-autocomplete.sh

popd > /bin/bash