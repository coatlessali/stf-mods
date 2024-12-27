#!/usr/bin/python
import sys

if len(sys.argv) < 2:
    print("No file(s) provided.")
    sys.exit()

for filename in sys.argv[1:]:
    dds = open(filename, "r+b")
    header = dds.read(3)
    if str(header) == "b\'DDS\'":
        print(f"Valid DDS header found in file {filename}.")
    else:
        pass

    if 'd5comp' in filename:
        print("Assuming file is compressed with DXT5 / BC3_UNorm.")
        dds.seek(8, 0)
        dds.write(b'\x07\x10\x00\x00')
        dds.seek(20, 0)
        dds.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x00\x00\x00\x04\x00\x00\x00\x44\x58\x54\x35\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    elif 'nocomp' in filename:
        print("Assuming file is uncompressed.")
        dds.seek(8, 0)
        dds.write(b'\x07\x10\x00\x00')
        dds.seek(20, 0)
        dds.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x00\x00\x00\x41\x00\x00\x00\x00\x00\x00\x00\x20\x00\x00\x00\x00\x00\xFF\x00\x00\xFF\x00\x00\xFF\x00\x00\x00\x00\x00\x00\xFF\x02\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    else:
        print(f"Did not find compression method in filename for file {filename}.\nPlease ensure your file is named correctly.")
sys.exit()
