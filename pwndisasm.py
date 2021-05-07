#!/usr/bin/python3
from pwn import *
import sys

context.arch = 'amd64'

shellcode_file = sys.argv[1]
shellcode_raw = ""

with open(shellcode_file, 'r') as f:
    shellcode_raw = f.read() 

print(disasm(asm(shellcode_raw)))
