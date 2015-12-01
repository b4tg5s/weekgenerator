#!/usr/bin/python3.4

import argparse
import random

def generate_week(nworkdays, nhours):
    weekdays = []
    for i in range(nworkdays):
        weekdays.append(-1)
    for i in range(7-nworkdays):
        weekdays.append(0)

    random.shuffle(weekdays)

    min_per_day = 3
    max_per_day = 5

    hours_left = nhours

    for i in range(len(weekdays)):
        if hours_left <= 0:
            break

        """ here i did not work """
        if weekdays[i] == 0:
            continue

        """ here i did work	"""
        hours = random.randint(min_per_day,max_per_day)
        hours_left = hours_left - hours
        weekdays[i] = hours

    for i in range(len(weekdays)):
        if weekdays[i] == -1:
            weekdays[i] = 0

    return weekdays


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--nweeks", default=1, type=int,
                            help='number of weeks to be generated. default is 1')
    parser.add_argument("--kw", action='store_true',
                            help='use and print kalenderwoche.')
    parser.add_argument("--first_kw", default=1, type=int,
                            help='specify the first kw if used with option --kw. defaults to 1')
    parser.add_argument("--weekhours", default=15, type=int,
                            help='worked hours in a week. output might deviate from the concrete value')

    args = parser.parse_args()

    start = args.first_kw

    for i in range(start, start+args.nweeks):
        print((str(i)+' ' if args.kw else '') + str(generate_week(random.randint(4,6), args.weekhours)))





