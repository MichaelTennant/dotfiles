#!/bin/bash

# 
# ~/.bash_profile
#

# Append to path
PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"
export PATH=$PATH

# Other global vars
export EDITOR=nvim
export TERM=alacritty

# Run ~/.bashrc
. ~/.bashrc
