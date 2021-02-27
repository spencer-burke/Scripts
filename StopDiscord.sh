#!/bin/bash
ps ax | grep "/app/discord/Discord" | head -n 1 | sed "s/[?].*//" | xargs kill

