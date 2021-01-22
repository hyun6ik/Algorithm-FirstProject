import sys
sys.stdin = open("input.txt", "rt")

# 내가 푼거
# a = list(input())
# tmp = []
# for i in a:
#     if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
#         continue
#     else:
#         i = int(i)
#         tmp.append(i)
#
# total = 0
# for i in range(len(tmp)):
#     total += tmp[i] * (10 ** (len(tmp)-(i+1)))
#
# cnt = 0
# for i in range(1,total+1):
#     if total % i == 0:
#         cnt +=1
#
# print(total)
# print(cnt)

s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)

cnt = 0
for i in range(1,res+1):
    if res % i == 0:
        cnt += 1

print(res)
print(cnt)




