#!/bin/python3
#https://www.hackerrank.com/challenges/dynamic-array/problem
N,Q = list(map(int ,input().split()));

a = [[] for i in range(N)]
lastans = 0 ;

for a_count in range(Q):
    qtype,x,y = list(map(int,input().split()));

    if qtype==1:
        a[(x^lastans)%N].append(y);
    else:
        seq=(x^lastans)%N;
        size = y%len(a[seq]) ;
        lastans = a[seq][size]
        print(lastans)