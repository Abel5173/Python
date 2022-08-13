w=input()
l=0
u=0
sp=0
sy=0
for i in w:
    if ord(i)==95:
        sp+=1
        continue
    if 33<=ord(i)<=64 or 91<=ord(i)<=96 or 123<=ord(i)<=126:
        sy+=1
    if 97<=ord(i)<=122:
        l+=1
    if 65<=ord(i)<=90:
        u+=1
sp/=len(w)
l/=len(w)
u/=len(w)
sy/=len(w)
print(sp)
print(l)
print(u)
print(sy)