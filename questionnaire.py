import argparse
import random
import sys

from words import read_dicts


def ask_question(word, definitions, tries=3):
    for _ in range(tries):
        answer = input("%s? " % word)
        if answer in definitions:
            return True

    return False


def ask_questions(input_file, reverse):
    word_to_defs, defs_to_words = read_dicts(input_file)
    d = defs_to_words if reverse else word_to_defs

    questions = list(d.keys())
    random.shuffle(questions)
    for question in questions:
        answers = d[question]
        result = ask_question(question, answers)
        print("[OK]" if result else "[FAIL]")
        print("  %s: %s" % (question, ", ".join(answers)))


parser = argparse.ArgumentParser()
parser.add_argument("input", type=argparse.FileType('r'))
parser.add_argument("--reverse", "-r", action="store_true")

args = parser.parse_args()

try:
    try:
        ask_questions(args.input, args.reverse)
    except KeyboardInterrupt:
        pass
    except EOFError:
        pass
finally:
    args.input.close()
