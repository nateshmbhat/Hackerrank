# https://www.hackerrank.com/contests/hourrank-24/challenges/strong-password



numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

n , s = int(input()) , input() ;

no_digits = 0 ; 
for i in numbers:
    no_digits+=s.count((i)) ;

no_lower = 0 ; 
for i in lower_case:
    no_lower+=s.count(i) ; 

no_upper = 0 ; 
for i in upper_case:
    no_upper+=s.count(i) ;

no_special = 0 ; 
for i in special_characters:
    no_special+=s.count(i) ; 


ans = 0 ; 

for i in [no_digits , no_lower , no_special , no_upper]:
    if not i:
        ans+=1 ;

if(ans+len(s)<6):
    ans+=(6-(ans+len(s))) ;

print(ans) ;

