#!/bin/bash

# Getting fan readings
for i in 0 1 2 3 4 5 6 7; do
    echo "level $i" > /proc/acpi/ibm/fan
    echo "level $i..."
    sleep 6
    cat /proc/acpi/ibm/fan | egrep "^speed"
    echo
done

# Restoring Defaults
echo "Restoring Defaults" 
echo "level auto" > /proc/acpi/ibm/fan

