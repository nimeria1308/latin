import unicodedata


def normalize_char(char):
    d = unicodedata.decomposition(char)
    if d:
        d = d.split(' ')[0]
        d = int(d, 16)
        return str(chr(d))
    else:
        return char


def normalize_word(word):
    return "".join([normalize_char(c) for c in word.strip()]).lower()


def parse_words(words):
    return [normalize_word(w) for w in words.split(',')]


def parse_line(line):
    words, definitions = line.split("-")
    words = parse_words(words)
    definitions = parse_words(definitions)
    return words, definitions


def add_definition(d, word, definition):
    if word not in d:
        d[word] = set()

    d[word].add(definition)


def read_dicts(f):
    word_to_defs = {}
    defs_to_words = {}

    for line in f:
        words, definitions = parse_line(line)
        for w in words:
            for d in definitions:
                add_definition(word_to_defs, w, d)
                add_definition(defs_to_words, d, w)

    return word_to_defs, defs_to_words
