# 1. 1부터 N까지 홀수출력하기
# n = int(input("숫자를 입력하세요 : "))


# i = 1
# while i <= n:
#     if i % 2 == 0:
#         i += 1
#         continue
#     else:
#         print(i)
#         i += 1

# for i in range(1, n+1):
#     if i % 2 == 1:
#         print(i)
#


# 2. 1부터 N까지의 합 구하기
#
# n = int(input("숫자를 입력해주세요 : "))
# score = 0
# for i in range(1, n+1):
#     if i % 2 == 1:
#         score += i
# print(score)

# 3. N의 약수 출력하기
n = int(input("숫자를 입력해주세요 : "))
for i in range(1, n+1):
    if n % i == 0:
        print(i, end= '')