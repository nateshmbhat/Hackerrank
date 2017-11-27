#https://www.hackerrank.com/challenges/icecream-parlor/problem

for a0 in range(int(input())):
    m = int(input())
    n , arr = input() , list(map(int , input().strip().split())) ;

    for i in range(len(arr)):
        try:
            for j in range(i+1, len(arr)):
                if(arr[i]+arr[j]==m):
                    print(i+1 , j+1) ;
        except:
            pass ; 