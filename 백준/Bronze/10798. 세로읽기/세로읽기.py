num = [list(input()) for _ in range(5)]

max = len(num[0])
for i in range(1, 5):
	if max < len(num[i]):
		max = len(num[i])
		
i=0
for i in range(max):
	for j in range(5):
		if (i >= len(num[j])):
			continue
		print(num[j][i], end='')