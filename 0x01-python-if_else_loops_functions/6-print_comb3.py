#!/usr/bin/python3
for n in range(100):
    if n % 10 > int(n/10):
        if n < 89:
            print("{:0>2d}".format(n), end=', ')
        else:
            print("{}".format(n))
