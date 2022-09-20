#!/usr/bin/python3
for n in range(100):
    if (n == 99):
        print("{:2d}".format(n), end='\n')
    else:
        print("{:0>2d}".format(n), end=', ')
