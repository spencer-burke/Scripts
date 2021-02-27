#!/bin/bash
# This script will kill the running discord process
ps ax | grep "/app/discord/Discord" | head -n 1 | sed "s/[?].*//" | xargs kill 2&> /dev/null

