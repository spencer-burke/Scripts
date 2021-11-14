#!/usr/bin/python3
import pefile

pe = pefile.PE("Path/To/DLLORPE")

# print("[INFO]: Printing Import Symbols")
# for entry in pe.DIRECTORY_ENTRY_IMPORT:
#     print(entry.dll)
#     for imp in entry.imports:
#         print("\t", hex(imp.address), imp.name)
print("[INFO]: Printing Export Symbols")
for entry in pe.DIRECTORY_ENTRY_EXPORT.symbols:
        print(hex(pe.OPTIONAL_HEADER.ImageBase + entry.address), entry.name.decode("utf-8"), entry.ordinal)

