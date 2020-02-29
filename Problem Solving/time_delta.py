#!/bin/python3
# Problem: https://www.hackerrank.com/challenges/python-time-delta/problem

from datetime import datetime as dt


# Complete the time_delta function below.
def time_delta(t1, t2):
    return print(t1 - t2)


if __name__ == '__main__':

    fmt = '%a %d %b %Y %H:%M:%S %z'

    for i in range(int(input())):
        t1 = dt.strptime(input(), fmt)
        t2 = dt.strptime(input(), fmt)
        print(int(abs((t1 - t2).total_seconds())))
