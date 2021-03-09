#!/bin/bash
echo "hex: $@"
echo -n "decimal: "
echo "ibase=16; $@"|bc

