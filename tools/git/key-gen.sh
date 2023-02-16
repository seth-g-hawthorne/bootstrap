#!/bin/bash
set -ue

email=$(git config -l | grep user.email | cut -f 2 -d =)
if [ -z "${email}" ]; then
  echo "git config user.email not set"
  exit 1
fi
ssh-keygen -t ed25519 -C "${email}"
ls ~/.ssh