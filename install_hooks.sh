#!/bin/bash

###################################################################
# title         : install_hooks.sh
# description   : Installs client side hooks for git
# author        : Abinav Ramesh Sundararaman
# date          : Oct 3, 2021
# version       : 1.0.0
# usage         : bash install_hooks.sh
# notes         : 
###################################################################

# remove files if it exists
rm -f .git/hooks/commit-msg
rm -f .git/hooks/pre-commit
rm -f .git/hooks/pre-rebase

# Create a symbolic link, to a file or directory. To learn more about symbolic links, please visit :
ln -s -f ../../hooks/commit-msg.py .git/hooks/commit-msg
ln -s -f ../../hooks/pre-commit.py .git/hooks/pre-commit
ln -s -f ../../hooks/pre-rebase.py .git/hooks/pre-rebase

# Provide execute permissions to files
chmod +x .git/hooks/commit-msg
chmod +x .git/hooks/pre-commit
chmod +x .git/hooks/pre-rebase
