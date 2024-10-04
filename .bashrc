#!/bin/bash

# 
# ~/.basrc
#

# If not running interactivley, don't do anything
[[ $- != *i* ]] && return

# Start xorg if not already running
[[ -z ${DISPLAY+x} ]] && startx

# Shell options
shopt -s autocd
shopt -s cdspell
shopt -s checkwinsize
shopt -s cmdhist
shopt -s dirspell
shopt -s globstar
shopt -s nocaseglob

# Aliases
alias ls='ls --color=auto'
alias grep='grep --color=auto'

alias dotfiles-git='git --git-dir=$HOME/.cfg/.git/ --work-tree=$HOME'

# Custom prompt (print newline before prompt if current line isn't empty)
function col {
    local COL
    local ROW
    IFS=';' read -sdR -p $'\E[6n' ROW COL
    echo "${COL}"
}

function __ps1_newline {
    if (( $(col) > 1)); then
        printf '\n'
    fi
}

PROMPT_COMMAND='__ps1_newline'
export PS1="\[\e[1;36m\][\u@\h: \W]$ \[\e[0m\]"

# A critical component of the system
# R.I.P. neofetch my beloved
fastfetch
