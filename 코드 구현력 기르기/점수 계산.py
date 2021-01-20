import sys
# sys.stdin = open("input.txt", "rt")

n = int(input())

a = list(map(int, input().split()))

cnt = 0
res = 0
for x in range(n):
    if a[x] == 1:
        cnt += 1
        res += 1 * cnt
    else:
        cnt = 0

print(res)

