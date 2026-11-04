"""Extract an Inspect .eval log (a zip archive whose entries use zstd compression).

Python's zipfile cannot read zstd entries (compression type 93), so this reads
each entry's raw bytes and decompresses them with the zstandard package.

Usage: python extract_eval.py LOG.eval OUT_DIR
Needs: pip install zstandard
"""
import os
import struct
import sys
import zipfile

import zstandard

ZSTD = 93


def extract(src, out):
    archive = zipfile.ZipFile(src)
    with open(src, "rb") as f:
        for info in archive.infolist():
            f.seek(info.header_offset)
            header = f.read(30)
            name_len, extra_len = struct.unpack("<HH", header[26:30])
            f.seek(info.header_offset + 30 + name_len + extra_len)
            data = f.read(info.compress_size)
            if info.compress_type == ZSTD:
                data = zstandard.ZstdDecompressor().decompress(data, max_output_size=200_000_000)
            path = os.path.join(out, info.filename)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "wb") as g:
                g.write(data)


if __name__ == "__main__":
    extract(sys.argv[1], sys.argv[2])
