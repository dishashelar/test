'''You are provided with two car manufacturing centers FACT1 & FACT2 denoted by an array, each producing the same models of cars but in different 
sequences. Your objective is to consolidate all the manufactured cars into a single warehouse, arranging them in a specific sequence represented
by the sequence number sq.
If sq is 0 then arrange it in ascending order. If sq is 1 then arrange it in descending order.'''
m=int(input())
fact1=[int(x) for x in input().split(' ')]
n=int(input())
fact2=[int(y) for y in input().split(' ')]
h=int(input())
fact=fact1+fact2
if(h==0):
    fact.sort()
    print(fact)
else:
    fact.sort()
    print(fact[::-1])
