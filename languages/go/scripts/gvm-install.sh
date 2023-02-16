#!/bin/bash
# See: https://github.com/moovweb/gvm
set -eu
sudo apt-get update 
sudo apt-get install bison
bash < <(curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)