# https://www.hackerrank.com/challenges/acm-icpc-team/problem

topics = [] 
topiclists = []
for a_0 in range(int(input().split()[0])):
    topics.append(int(input() , 2)) ;

for i in range(len(topics)):
    for j in range(i+1 , len(topics)):
        topiclists.append(bin((topics[i] | topics[j])).count('1'));
 


maxtopic = max(topiclists) ; 
numofteams = topiclists.count(maxtopic) ; 
print(maxtopic , numofteams , sep='\n') ;


