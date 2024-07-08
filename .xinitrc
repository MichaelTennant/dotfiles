#!/bin/bash

# 
# ~/.xinitrc
#

# Startup apps
flameshot &
picom &
xscreensaver --no-splash &

# Start Qtile
qtile start
