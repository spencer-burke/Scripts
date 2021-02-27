#!/bin/bash
# This script will kill the running slack process
ps ax | grep /app/extra/lib/slack | head -n 1 | sed "s/[?].*//" | xargs kill 2&> /dev/null

