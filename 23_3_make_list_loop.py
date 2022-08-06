# for 로 1차원 리스트 만들기
a = []
for i in range(10):
    a.append(i)
print(a)
print()

# for로 2차원 리스트 만들기
a = []
for i in range(3):
    line = []
    for j in range(2):
        line.append(j)
    a.append(line)
print(a)
print()

# 리스트 표현식으로 2차원 리스트 만들기
a = [[0 for j in range(2)] for i in range(3)]
print(a)

b = [[0] * 2 for i in range(3)]
print(b)
print()

# 톱니형 리스트 만들기
a = [3, 1, 3, 2, 5]
b = []

for i in a:
    line = []
    for j in range(i):
        line.append(j)
    b.append(line)
print(b)
print()

b = [[0 for j in range(i)] for i in a]
print(b)
c = [[0] * i for i in a]
print(c)
print()

# 2차원 리스트 정렬하기
# sorted(반복가능한객체, key=정렬함수, reverse=True 또는 False)
student = [["john", "C", 19], ["maria", "A", 25], ["andrew", "B", 7]]
print(sorted(student, key=lambda student: student[1]))
print(sorted(student, key=lambda student: student[2]))
