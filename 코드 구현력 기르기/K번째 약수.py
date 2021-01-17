import sys
# sys.stdin = open("input.txt", "rt")

# n, k = map(int, input().split())
# cnt = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         cnt += 1
#     if cnt == k:
#         print(i)
#         break
# else:
#     print(-1)


def main():
    n, k = map(int, input().split())

    list_n = []
    for x in range(1, n + 1):
        if n % x == 0:
            list_n.append(x)

    if len(list_n) < k:
        print(-1)
    else:
        print(list_n[k - 1])


if __name__ == "__main__":
    main()
