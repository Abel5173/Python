n= int(input())
l=[]
l = [int(x) for x in input().split()]
s=(n*(n+1))/2
m=int(s-sum(l))
print(m)