#!/bin/bashh
# Installs kubectx and kubens
# Ref: https://github.com/ahmetb/kubectx
#
sudo git clone https://github.com/ahmetb/kubectx /usr/local/kubectx
sudo ln -s /usr/local/kubectx/kubectx /usr/local/bin/kubectx
sudo ln -s /usr/local/kubectx/kubens /usr/local/bin/kubens
