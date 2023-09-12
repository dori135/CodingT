n = int(input())
num = list(map(int, input().split()))
m = max(num)
sum = 0
for i in range(n):
    sum += num[i]/m*100
print(sum/n)