"""Split an amount in cents exactly, distributing leftover cents one per person."""

import argparse


def positive(text):
    value = int(text)
    if value < 1:
        raise argparse.ArgumentTypeError("Expected an integer of at least 1")
    return value


def nonnegative(text):
    value = int(text)
    if value < 0:
        raise argparse.ArgumentTypeError("Expected an integer of at least 0")
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cents", type=nonnegative)
    parser.add_argument("people", type=positive)
    args = parser.parse_args()
    try:
        base, extra = divmod(args.cents, args.people)
        if extra:
            print(f"{extra} participant(s) pay {base + 1} cents each")
        if args.people > extra:
            print(f"{args.people - extra} people pay {base} cents each")
    except ValueError as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
