import sys


def main():
    argv_len = len(sys.argv)
    assert argv_len <= 2, "more than one argument is provided"

    if argv_len < 2:
        return

    num_arg = sys.argv[1]
    if num_arg is False:
        return

    try:
        num = int(num_arg)
    except ValueError:
        raise AssertionError("argument is not an integer")

    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd")


if __name__ == '__main__':
    try:
        main()
    except AssertionError as error:
        print(f"AssertionError: {error}")
