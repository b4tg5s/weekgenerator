#!/usr/bin/python3.4

import argparse
import random

""" vars """
min_per_day = int()
max_per_day = int()
weekends = bool()


def generate_week(nworkdays, nhours):
    weekdays = []
    for i in range(nworkdays):
        weekdays.append(-1)
    for i in range((7 if weekends else 5)-nworkdays):
        weekdays.append(0)

    random.shuffle(weekdays)

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

    """ flags """
    parser.add_argument("--kw", action='store_true',
                            help='use and print kalenderwoche.')
    parser.add_argument("--first_kw", default=1, type=int,
                            help='specify the first kw if used with option --kw. defaults to 1')
    parser.add_argument("--we", action='store_true',
                            help='worked on weekends. implicitly true if work days is greater 5')

    """ parameters """
    parser.add_argument("--weekhours", default=15, type=int,
                            help='worked hours in a week. output might deviate from the concrete value')
    parser.add_argument("--hmin", default=3, type=int,
                            help='hours at least worked per day. defaults to 3.' )
    parser.add_argument("--hmax", default=5, type=int,
                        help='hours at most worked per day. defaults to 5.' )
    parser.add_argument("--dmin", default=5, type=int,
                        help='days at least worked per week. defaults to 5.' )
    parser.add_argument("--dmax", default=5, type=int,
                        help='days at most worked per week. defaults to 5.' )


    args = parser.parse_args()

    assert(args.hmin <= args.hmax)
    assert(args.dmin <= args.dmax)
    min_per_day = args.hmin
    max_per_day = args.hmax

    weekends = args.we
    if args.dmax > 5:
        weekends = True

    start = args.first_kw
    for i in range(start, start+args.nweeks):
        workdays = random.randint(args.dmin, args.dmax)
        print((str(i)+' ' if args.kw else '') + str(generate_week(workdays, args.weekhours)))





