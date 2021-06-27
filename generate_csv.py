import argparse
import sys

from words import read_dicts


def convert_to_csv(input_file, output_file, reverse):
    word_to_defs, defs_to_words = read_dicts(input_file)
    d = defs_to_words if reverse else word_to_defs

    for word in sorted(d.keys()):
        defs = ", ".join(sorted(d[word]))
        output_file.write("%s|%s\n" % (word, defs))


parser = argparse.ArgumentParser()
parser.add_argument("input", type=argparse.FileType('r'))
parser.add_argument("--reverse", "-r", action="store_true")
parser.add_argument(
    "--output", "-o", type=argparse.FileType('w'), default=sys.stdout)

args = parser.parse_args()

try:
    convert_to_csv(args.input, args.output, args.reverse)
finally:
    if args.output != sys.stdout:
        args.output.close()
    args.input.close()
