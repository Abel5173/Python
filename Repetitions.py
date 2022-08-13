s=input()
maxCount=0
for i in range(len(s)):
    count=1
    for j in range(i+1, len(s)):
        if s[i]==s[j]:
            count+=1
        else:
            break
    maxCount=max(maxCount, count)
print(maxCount)