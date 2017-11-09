#https://www.hackerrank.com/challenges/the-hurdle-race/problem

#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
# your code goes here

print("0" if k>max(height) else max(height)-k) ;
