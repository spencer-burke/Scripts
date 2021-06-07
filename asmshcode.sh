#!/bin/bash

# $1=name of the shellcode.s file
# $2=name of the shellcode ELF file
# $3=name of the shellcode RAW file

gcc -Wl,-N --static -nostdlib $1 -o $2
objcopy --dump-section .text=$3 $2
