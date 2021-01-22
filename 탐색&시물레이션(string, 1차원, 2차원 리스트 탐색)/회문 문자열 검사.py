import sys
sys.stdin = open("input.txt", "rt")

# 내가 푼거
# n = int(input())
# a = []
# for i in range(n):
#     tmp = []
#     b = list(input().lower())
#     for j in range(len(b), 0, -1):
#         b[j-1].lower()
#         tmp.append(b[j-1])
#     if b == tmp:
#         print("#{0} YES".format(i+1))
#     else:
#         print("#{0} NO".format(i+1))

# 1번풀이
# n = int(input())
# for i in range(n):
#     s = input()
#     s = s.upper()
#     size = len(s)
#     for j in range(n//2):
#         if s[j] != s[-1-j]:
#             print("#%d NO" %(i+1))
#             break
#     else:
#         print("#%d YES" %(i+1))

n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))