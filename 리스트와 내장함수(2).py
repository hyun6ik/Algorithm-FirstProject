a = [23, 12, 36, 53, 19]
# print(a[:3])
# print(a[1:4])
#
# print(len(a))
#
# for i in range(len(a)):
#     print(a[i], end=' ')
# print()
#
# for x in a:
#     print(x, end=' ')
# print()
#
# for x in a:
#     if x % 2 == 1:
#         print(x, end=' ')
# print()
#
# for x in enumerate(a):
#     print(x, end=' ')
# print()
#
# for x in enumerate(a):
#     print(x[0], x[1])
# print()
#
# for index, value in enumerate(a):
#     print(index, value)
# print()

if all(60>x for x in a):
    print("YES")
else:
    print("NO")

if any(15>x for x in a):
    print("YES")
else:
    print("NO")
