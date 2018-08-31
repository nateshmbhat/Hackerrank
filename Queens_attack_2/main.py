# https://www.hackerrank.com/challenges/queens-attack-2/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    t , r , b , l = n-r_q , n - c_q , r_q-1 , c_q -1  ; 
    tl , tr , bl ,br  = min(t , l ) , min(t , r) , min(b , l) , min(b , r) ;

    x_q , y_q = c_q , r_q ; 
    
    for obstacle in obstacles:
        y , x = obstacle ; 
        if(abs(x-x_q) == abs(y-y_q)   or  x==x_q or y==y_q):
                t = min(t , y-y_q -1  if(x==x_q and y!=y_q and y>y_q) else t ) ;
                b = min(b , y_q - y -1  if(x==x_q and y!=y_q and y<y_q) else b ) ;
                l = min(l , x_q - x -1  if(x!=x_q and y==y_q and x_q>x ) else l ) ;
                r = min(r , x - x_q -1  if(x!=x_q and y==y_q and x_q < x ) else r ) ;
                tl = min(tl , y-y_q -1 if(x<x_q and y>y_q) else tl ) ;  
                tr = min(tr , x - x_q -1 if(x>x_q and y>y_q) else tr ) ;  
                bl = min(bl , x_q - x -1 if(x<x_q and y<y_q) else bl ) ;  
                br = min(br , x-x_q-1 if(x>x_q and y<y_q) else br ) ;
                
    return sum([t,b,l , r, tl , tr , bl , br]) ;


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(str(result) + '\n')

