#!/bin/bash
# 
set -eu

echo       "Configure git"
read -r -p "  Name (first last): " name
read -r -p "  Email            : " email
while true
do
      read -r -p "  Confirm (y/n)    : " confirm
 
      case $confirm in
            [yY])
                  break
                  ;;
            [nN])
                  exit 1
                  ;;
            *)
                  echo "    Enter y or n"
                  ;;
      esac      
done

git config --global color.ui true
git config --global user.name "${name}"
git config --global user.email "${email}"
git config --global push.default current
git config -l