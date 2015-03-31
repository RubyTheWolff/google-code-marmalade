#!/usr/bin/env python3

import jam

def parse_arguments(credit, num_items, prices):
    return int(credit), int(num_items), str(prices)

def two_items(credit, num_items, prices):
    credit, num_items, prices = parse_arguments(credit, num_items, prices)

    prices_list = [int(p) for p in prices.split(' ')]
    for idx1, price1 in enumerate(prices_list):
        for idx2, price2 in enumerate(prices_list):
            if idx1 != idx2:
                if price1 + price2 == credit:
                    two_indexes = sorted((idx1 + 1, idx2 + 1))
                    return ' '.join(map(str, two_indexes))

def main():
    jam.output(two_items)

if __name__ == '__main__':
    main()
