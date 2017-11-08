# https://www.hackerrank.com/challenges/separate-the-numbers/problem

for a0 in range(int(input())):
    s = input();
    sublen = 1 ;
    yes  = 0 ;
    while(sublen<=len(s)/2):
        start = s[0:sublen] ;
        i =1 ;
        while(len(start)<len(s)):
            start = start+str(int(s[0:sublen])+i) ;
            i+=1 ;

        if(start==s):
            print("YES"  , s[0:sublen]) ;
            yes = 1 ;
            break ;
        else:
            sublen+=1 ;

    if not yes :print("NO") ;


