s  = input()
ss = []
for i in range(len(s)):
    ss.append(s[i:])
ss.sort()
for i in range(len(s)):
    print(ss[i])