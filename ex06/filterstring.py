import sys

def is_str(string: str) -> bool:
    """Check if given argument is a str"""
    return str and type(string) == str

def str_is_int(string: str) -> bool:
    """Check if given argument (str) is convertable to int type"""
    try:
        int(string)
        final_state = True
    except:
        final_state = False
    return final_state

def count_special(text: str) -> int:
    """Count punctuation characters and non-breaking spaces in text."""
    specials = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    specials.add('\u00A0')
    return sum(1 for c in text if c in specials)

def parse_arguments() -> bool:
    """"Check if given arguments are valid"""
    return len(sys.argv) == 3 and\
        is_str(sys.argv[1]) and count_special(sys.argv[1]) == 0 and\
        str_is_int(sys.argv[2])

def main():
    assert parse_arguments(), "the arguments are bad"

    new_list = []
    target_text = sys.argv[1]
    max_length = int(sys.argv[2])

    for value in target_text.split():
        if len(value) >= max_length:
            new_list.append(value)
    print(new_list)

if __name__ == '__main__':
    try:
        main()
    except AssertionError as error:
        print(f"AssertionError: {error}")
