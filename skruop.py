n=int(input())
a=7
for i in range(n):
    S=input()
    if S=="Skru op!":
        a+=1
        if a>10:
            a=10
    else:
        a-=1
        if a<0:
            a=0
print(a)