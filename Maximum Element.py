#https://www.hackerrank.com/challenges/maximum-element/problem

mylist = [];
maxlist = []
count = 0;

for _ in range(int(input())):

    a = [int(i) for i in input().strip().split()]
    if a[0] == 1:

        if not len(maxlist):
            maxlist.append(a[1])
        else:
            if a[1]>=maxlist[-1]:
                maxlist.append(a[1])
        mylist.append(a[1])


    elif a[0] == 2:

        if maxlist[-1] == mylist[-1]:
            mylist = mylist[:-1]
            maxlist = maxlist[:-1]
        else:
            mylist = mylist[:-1]
    else:
        print(maxlist[-1])