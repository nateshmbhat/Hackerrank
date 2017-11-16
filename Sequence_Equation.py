# https://www.hackerrank.com/challenges/permutation-equation/problem

a, n  = {}  , input()  ;

for ind , ele in enumerate(list(map(int , input().split()))):
	a[ele] = ind+1 ;
for i in range(1 , int(n)+1):
	print(a[a[i]]) ;


# Still better pythonion code : 

# n  = int(input()) ; 
# a = [int(i) for i in input().split()] ;
# for i in range(1 , n+1):
# 	print(a.index(a.index(i))) ;
