#!/usr/bin/python3
import sys

rstr = sys.argv[1]

rstr = rstr[::-1]
cstr = ""

for c in rstr:
        cstr += hex(ord(c))[2::]  
cstr = "0x" + cstr

sys.stdout.buffer.write(cstr.encode())
print()
