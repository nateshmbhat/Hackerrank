#https://www.hackerrank.com/challenges/equal-stacks

stacks = [[int(i) for i in input().strip().split()] for _ in range(len(input().split()))]
height = [sum(i) for i in stacks]
while(len(set(height))!=1):
    index = height.index(max(height));
    height[index]-= stacks[index].pop(0)
print(height[0])

"""

Read the first line and split it on the spaces to see how many stacks there are.
Read each line of numbers, convert to a queue and store them all in an array.
Create another array that contains the heights of all the stacks. This is so we don't have to repeatedly sum the blocks in the stacks.
While the stacks don't all have the same height compute the maximum height, find the index of the elem in heights that has that value then pop off the first elem in the corresponding stack and subtract from the height stored in heights array.
Print out the height of the first (or any other) stack.

"""



