cnt = 0
for n in range(1, 10):
    if n % 2 == 0:
        print(n)
        cnt += 1
else:
    print(f"We have {cnt} even numbers")
