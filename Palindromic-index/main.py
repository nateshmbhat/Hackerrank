# https://www.hackerrank.com/challenges/palindrome-index/problem


#!/bin/python3

import math
import os
import random
import re
import sys

def checkpalindrome(s):
    return s==s[::-1] ;


# Complete the palindromeIndex function below.
def palindromeIndex(s):
    n = len(s)-1 ; 
    s_original = s ; 
    if(checkpalindrome(s)):return -1 ;  
    for i in range(n//2):
        if(s[i]!=s[n-i]):
            a = s[0:i]+s[i+1 : ] ; 
            b = s[0:n-i]+s[n-i+1:];
            if(checkpalindrome(a)):return a ; 
            if(checkpalindrome(b)):return b ;
        

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        print(str(result) + '\n')

