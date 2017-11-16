#https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

import json


for a0 in range(int(input())):
    s = input() ; 
    stack = [] ;
    hack = "hackerrank" ;
    pointer = 0 ;

    for i in s:
        if("".join(stack)==hack): break ;
        if i==hack[pointer]:
            if not stack:
                stack.append(i) ;
                pointer+=1 ;
            if(stack[-1]!=i or (i=='r' and stack.count('r')<2)):
                stack.append(i) ;
                pointer+=1 ;
    print("YES" if("".join(stack)=="hackerrank" ) else "NO") ;