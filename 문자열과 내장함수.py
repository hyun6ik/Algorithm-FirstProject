msg = "It is Time"
#
# print(msg.upper())
# print(msg.lower())
# print(msg)
#
tmp = msg.upper()
# print(tmp)
#
# # index 0부터 시작
# print(tmp.find('T'))
# print(tmp.count('T'))
# print(msg[:2])
# print(msg[3:5])
# print(msg[6:])

# print(len(msg))
# for i in range(len(msg)):
#     print(msg[i], end=' ')
# print()
#
# for x in msg:
#     print(x, end='')
# print()

# for x in msg:
#     if x.isupper():
#         print(x, end=' ')
# print()
#
# for x in msg:
#     if x.islower():
#         print(x, end = ' ')
# print()
# for x in msg:
#     if x.isalpha():
#         print(x, end= '')

# 아스키코드
# A = 65 Z = 90
# a = 97 z = 122
tmp = 'AZ'
for x in tmp:
    print(ord(x))
temp = 'az'
for x in temp:
    print(ord(x))

tmp = 65
print(chr(tmp))