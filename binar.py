n=input()
w=[]
x=[]
y=[]
z=[]
for i in range(0,4):
     a=str(f"{int(n[i]):04b}")
     if i==0:
        w=list(a)
     if i==1:
        x=list(a)
     if i==2:
        y=list(a)
     if i==3:
        z=list(a)
for i in range(4):
    if w[i]=="0":
        print(".",end="")
    else:
        print("*",end="")
    if x[i]=="0":
        print(".",end="")
    else:
        print("*",end="")
    print(" ",end="")
    if y[i]=="0":
        print(".",end="")
    else:
        print("*",end="")
    if z[i]=="0":
        print(".",end="")
    else:
        print("*",end="")
    print()
# . *   . .
# . .   . .
# . .   * .
# . .   * .
# . *   . . 
# . .   . .
# . .   * .
# . .   * .
