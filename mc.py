#!/usr/bin/env python3

""" Money Converter """

import requests
from argparse import ArgumentParser

VALID_CHOICES = ["in", "to", "from"]

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("amount", metavar="amount", type=float)
    parser.add_argument("currency 1", metavar="currency1", type=str)
    parser.add_argument(
        "conversion direction", type=str, default="in", choices=VALID_CHOICES
    )
    parser.add_argument("currency 2", metavar="currency2", type=str)
    return parser.parse_args()


def main():
    args = parse_args()
    amount = args.amount
    c1 = getattr(args, "currency 1").upper()
    c2 = getattr(args, "currency 2").upper()
    url = f"https://api.exchangerate-api.com/v4/latest/{c1}"
    json = requests.get(url).json()
    rate = json["rates"][c2]
    new_amount = amount * rate
    print(f"{amount:.2f}", c1, "equals", f"{new_amount:.2f}", c2)


if __name__ == "__main__":
    main()
