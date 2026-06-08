import sys

NESTED_MORSE = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",

    ".": "",
    ",": "",
    "?": "",
    "'": "",
    "!": "",
    "/": "",
    "(": "",
    ")": "",
    "&": "",
    ":": "",
    ";": "",
    "=": "",
    "+": "",
    "-": "",
    "_": "",
    '"': "",
    "$": "",
    "@": "",

    " ": "/",

    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}


def is_str(string: str) -> bool:
    """Check if given argument is a str"""
    return str and type(string) is str


def count_special(text: str) -> int:
    """Count punctuation characters and non-breaking spaces in text."""
    specials = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    specials.add('\u00A0')
    return sum(1 for c in text if c in specials)


def parse_arguments() -> bool:
    """"Check if given arguments are valid"""
    return len(sys.argv) == 2 and\
        is_str(sys.argv[1]) and count_special(sys.argv[1]) == 0


def main():
    assert parse_arguments(), "the arguments are bad"
    target_text = sys.argv[1].lower()
    target_len = len(target_text)
    final_text = ""

    for x in range(0, len(target_text)):
        final_text = final_text + NESTED_MORSE[target_text[x]] +\
            (x < (target_len - 1) and " " or "")
    print(final_text)


if __name__ == '__main__':
    try:
        main()
    except AssertionError as error:
        print(f"AssertionError: {error}")
