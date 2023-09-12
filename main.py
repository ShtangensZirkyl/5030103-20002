a = 'I\'m'

b = ['a', 1, 3]

# print(b)
#
# b = list()
# b.append(1)
# b.insert(0, 'str')

# b.pop(0)
# b.remove('str')

for el in b:
    print(el)

print()

for i in range(len(b)):
    print(b[i])

print()

i = 0
while i < 3:
    print(b[i])
    i += 1

print()

i = 0
while True:
    print(b[i])
    i += 1
    if i > 2:
        break

for i, el in enumerate(b):
    print('Index: ' + str(i) + ', element: ' + str(el))

a = [[1, 2, 3], [3, 2, 1]]
# print(a[0][2])
a[0][2] = 2 ** a[0][2]
# print(a[0][2])

i = 2
l = [i + 1 for k in range(10)]
print(l[1])

# d = dict()
d = {'key_word': 'a', 2: 'b'}
# d_2 = dict.fromkeys(range(10))
d_2 = {key: value for key in range(10) for value in range(10, 50, 2)}
print(d_2)

if 'd' in d.values():
    # for k in d.keys():
    #     print(k)
    print('Yes')
elif 'b' in d.values():
    print('b exists')
else:
    print('No such key')

d.update({'second_key_word': 'b'})
print()
# d.pop(2)
print(d)

# print(b)
# b[1] = ' '
# b = str(b)