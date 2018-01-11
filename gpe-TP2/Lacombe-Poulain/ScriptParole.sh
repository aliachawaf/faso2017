#!-/bin/bash
pico2wave -l fr-FR -w temp.wav "$1"
omxplayer temp.wav
