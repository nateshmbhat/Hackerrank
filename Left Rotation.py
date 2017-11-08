#https://www.hackerrank.com/challenges/array-left-rotation?h_r=next-challenge&h_v=zen

n , d = [int(i) for i in input().split()]

arr = [int(i) for i in input().split()]

arr_copy = list(arr)

for count in range(n):
	arr[count] = arr_copy[(count+d)%n]

print(" ".join([str(i) for i in arr]))