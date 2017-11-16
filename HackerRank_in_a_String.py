#https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

import json


for a0 in range(len(input())):
    s = input() ; 
    stack = [] ;
    hack = "hackerrank" ;
    pointer = 0 ;

    for i in s:
    
        if i==hack[pointer]:
            if not stack:
                stack.append(i) ;
                pointer+=1 ;
            if(stack[-1]!=i or (i=='r' and stack.count('r')<2)):
                stack.append(i) ;
                pointer+=1 ;
    print("YES" if("".join(hack)=="hackerrank") else "NO") ;