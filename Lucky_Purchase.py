#https://www.hackerrank.com/contests/w35/challenges/lucky-purchase/problem
books= {} ;
n= int(input()) ;
for a0 in range(n):
    string = input().split() ;
    books[string[0]] = string[1] ;


books = list(books.items()) ;
mini = books[0] ;

for pair in books:
    if pair[1].count('7')+pair[1].count('4')!=len(pair[1]):
        continue;
    if(pair[1].count('7')==pair[1].count('4')):
            if(int(pair[1])<int(mini[1])):
                mini = pair ;

print(mini[0] if mini[1].count('7')==mini[1].count('4') and mini[1].count('7')+mini[1].count('4')==len(mini[1]) else "-1") ;