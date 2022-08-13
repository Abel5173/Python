n = input()
n = n.replace('-', '')
a = 4*int(n[0]) + 3 * int(n[1]) + 2 * int(n[2])+7*int(n[3])+6*int(n[4])+5 * \
    int(n[5])+4*int(n[6])+3*int(n[7])+2*int(n[8])+1*int(n[9])
if a % 11 == 0:
    print(1)
else:
    print(0)
