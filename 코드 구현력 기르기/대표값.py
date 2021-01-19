import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
a = list(map(int, input().split()))

average = sum(a)/N
average += 0.5
average = int(average)

min = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x - average)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1

print(average, res)

