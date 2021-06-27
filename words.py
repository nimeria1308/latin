import pprint


def parse_words(words):
    return [w.strip() for w in words.split(',')]


def parse_line(line):
    words, definitions = line.split("-")
    words = parse_words(words)
    definitions = parse_words(definitions)
    return words, definitions


def read_word_dict(f):
    word_dict = []

    for line in f:
        print(line)
        words, definitions = parse_line(line)
        word_dict.append((words, definitions))

    return word_dict


with open("words.txt") as f:
    word_dict = read_word_dict(f)
    pprint.pprint(word_dict)
