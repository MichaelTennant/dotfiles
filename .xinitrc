#!/bin/bash

# 
# ~/.xinitrc
#

# Startup apps
flameshot &
otd-daemon &
picom &
syncthing &
xscreensaver --no-splash &

# Start Qtile
qtile start
