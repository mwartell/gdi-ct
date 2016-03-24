#!/usr/bin/python3

import csv
import random
import sys

def id_numbers(start=1011, step=100):
    """Returns a series of increasing integers starting at start.
       The next number will be at most step above the last.
    """
    while True:
        yield start
        start += random.randint(1, step)


def fake_data(outf, n=20):
    """Write n rows of fake data to outf."""
    csvw = csv.writer(outf)
    idn = id_numbers()
    for i in range(n):
        # case number, sex, flavor
        csvw.writerow([idn.next(), random.choice('mf'), random.choice('ps')])

if __name__ == '__main__':
    fake_data(sys.stdout)

