s=input()
temp=''
for i in s:
    if temp==i:
        continue
    print(i,end='')
    temp=i