#https://www.hackerrank.com/challenges/game-of-two-stacks

for _ in range(int(input())):
    a,b,x = [int(i) for i in input().strip().split()]
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    mysum = 0
    count =0
    while(1):
        mysum+=(A.pop(0) if (A and A[0]<B[0]) else B.pop(0) if B else 0)

        if not (A or B):
            break;

        if mysum>x:
            break;
        count+=1

    print(count)


