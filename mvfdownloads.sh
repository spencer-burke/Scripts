#!/bin/bash
mv "/home/"$USER"/Downloads/"$(ls -t1 ~/Downloads | head -n 1) $(pwd)
