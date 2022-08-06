# 2차원 리스트
# 리스트 = [[값, 값], [값, 값], [값, 값]]
a = [[10, 20], [30, 40], [50, 60]]
print(a)
b = [[10, 20], [30, 40], [50, 60]]
print(b)

# 2차원 리스트 요소에 접근하기
# 리스트[세로인덱스][가로인덱스]
# 리스트[세로인덱스][가로인덱스] = 값
print(a[0][0])
print(a[1][1])
print(a[2][1])
a[0][1] = 1000
print(a[0][1])

b = ([10, 20], [30, 40], [50, 60])
b[0][1] = 50
print(b)

from pprint import pprint

pprint(b, width=20, indent=4)
print()

# 2차원 리스트 출력하기
a = [[10, 20], [30, 40], [50, 60]]
for x, y in a:
    print(x, y)

for i in a:
    for j in i:
        print(j, end=" ")
    print()
print()

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()
print()

i = 0
while i < len(a):
    x, y = a[i]
    print(x, y)
    i += 1
print()

i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end=" ")
        j += 1
    i += 1
    print()
print()
