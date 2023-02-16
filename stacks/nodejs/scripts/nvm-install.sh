#!/bin/bash
set -eu
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
echo "export NVM_COLORS='cmgRY'" ~/.profile
source ~/.profile
source ~/.bashrc
nvm list-remote 
