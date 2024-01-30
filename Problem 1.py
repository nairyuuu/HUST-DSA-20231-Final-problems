#Problem 1:
n, Q = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if A[i] + A[j] >= Q:
            cnt += 1
print(cnt) 
