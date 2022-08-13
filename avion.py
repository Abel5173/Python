from operator import truediv


b=True
l=[]
for i in range(1, 6):
    s=input()
    if s.find('FBI') != -1:
        l.append(i)
        b=False
if b :
    print('HE GOT AWAY!')
else:
    for i in l:
        print(i, end=' ')