n = int(input())
m = int(input())
k = int(input())
arr = [0] * n
for i in range(m):
   arr[i] = int(input())
ans = 0
arr.sort()
if k > 0:
   for i in range(k + 1, m + 3, 1):
       ans = max(ans, arr[i] - arr[i - k - 1] - 1)
else:
   j = 0
   while arr[j] == 0:
       j = j + 1
   count = 0
   for i in range(1, n + 1, 1):
       count += 1
       if j < n and (i == arr[j]):
           count = 0

           j += 1
       ans = max(count, ans)
print(ans)