#https://www.hackerrank.com/challenges/balanced-brackets
stack = [] 
store = {')':'(' , ']' :'[' , '}':'{'}
for _ in range(int(input())):
    stack.clear()
    for i in input():
        if stack and store.get(i)==stack[-1]:
            stack.pop()
        else:stack.append(i)
    print("NO" if stack else "YES")