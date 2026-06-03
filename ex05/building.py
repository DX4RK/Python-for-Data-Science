import sys


def count_uppercases(text: str) -> int:
    """"Count the uppercases in text and return it."""
    return sum(1 for c in text if c.isupper())


def count_lowercases(text: str) -> int:
    """"Count the lowercases in text and return it."""
    return sum(1 for c in text if c.islower())


def count_punctuations(text: str) -> int:
    """"Count the punctuation marks in text and return it."""
    punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    return sum(1 for c in text if c in punctuations)


def count_spaces(text: str) -> int:
    """"Count the spaces in text and return it."""
    return sum(1 for c in text if c.isspace())


def count_digits(text: str) -> int:
    """"Count the digits in text and return it."""
    return sum(1 for c in text if c.isdigit())


def main():
    arg_len = len(sys.argv)
    assert arg_len <= 2, "more than one argument is provided"

    target_text = (arg_len > 1) and\
        sys.argv[1] or input("What is the text to count?\n")

    print(f"The text contains {len(target_text)} characters:")
    print(f"{count_uppercases(target_text)} upper letters")
    print(f"{count_lowercases(target_text)} lower letters")
    print(f"{count_punctuations(target_text)} punctuation marks")
    print(f"{count_spaces(target_text)} spaces")
    print(f"{count_digits(target_text)} digits")


if __name__ == '__main__':
    try:
        main()
    except AssertionError as error:
        print(f"AssertionError: {error}")
