
import os
import sys
import argparse
import patcher


def pathSplit(path):
    basePath, name = os.path.split(path)
    baseName, ext = os.path.splitext(name)
    return basePath, baseName, ext


def getArgs():
    """ get command line arguments """

    desc = 'BPS Patcher'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('InputRom', help="input rom file")
    parser.add_argument('InputBPS', help="input bps file")
    args = parser.parse_args()
    return args


def main():

    args = getArgs()
    _, n, e = pathSplit(args.InputRom)
    p, pn, _ = pathSplit(args.InputBPS)

    op = os.path.join(p, pn + e)

    with open(args.InputBPS, "rb") as f:
        base_patch = f.read()

    with open(args.InputRom, "rb") as f:
        source = f.read()

    instance = patcher.BPSPatch(base_patch)
    base_patched = instance.patch_rom(source)

    with open(op, "wb") as f:
        f.write(base_patched)


if __name__ == '__main__':
    main()
