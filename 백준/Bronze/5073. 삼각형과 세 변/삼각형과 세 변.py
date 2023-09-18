def tri(n, m, k):
	a = sorted([n, m, k])
	if a[0]+a[1] <= a[2]:
		return "Invalid"
	if a[0] == a[1]:
		if a[1] == a[2]:
			return "Equilateral"
		else:
			return "Isosceles"
	else:
		if a[1] == a[2]:
			return "Isosceles"
		else:
			return "Scalene"

n, m, k =map(int, input('').split())
while not(n == 0 and m == 0 and k==0):
	print(tri(n, m, k))
	n, m, k =map(int, input('').split())