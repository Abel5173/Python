from re import M
import string

s = input()
a = s[0:int(len(s)/2)]
b = s[int(len(s)/2):]
m = string.ascii_uppercase
sm1 = 0
sm2 = 0
d = str
c = str
for i in a:
    sm1 += m.index(i)
for i in b:
    sm2 += m.index(i)

a = list(a)
b = list(b)

for i in range(len(a)):
    a[i] = m[(m.index(a[i])+sm1) % 26]
for i in range(len(b)):
    b[i] = m[(m.index(b[i])+sm2) % 26]
for i in range(len(a)):
    a[i] = m[(m.index(a[i])+m.index(b[i])) % 26]
print("".join(a))
