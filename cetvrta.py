from posixpath import split

x_l = []
y_l = []
for i in range(3):
    x, y = map(int, input().split())
    x_l.append(x)
    y_l.append(y)
# print(x_l)
# print(x_l.count(5))
for i in range(3):
    if x_l.count(x_l[i]) == 1:
        print(x_l[i], end=' ')
for i in range(3):
    if y_l.count(y_l[i]) == 1:
        print(y_l[i])
