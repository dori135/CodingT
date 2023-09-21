import sys
n, k = map(int,sys.stdin.readline().split())
num = []
i = n-1
m = 0
for i in range(n):
	num.append(int(sys.stdin.readline()))
while(i >= 0):
	if k > num[i]:
		m += int(k/num[i])
		k -= int(k/num[i])*num[i]
	elif k == num[i]:
		m += 1
		break
	elif k == 0:
		break
	else:
		i-=1
print(m)
