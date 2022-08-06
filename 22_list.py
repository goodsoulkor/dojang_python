# 리스트 표현식
# 리스트 컴프리헨션(list comprehension) - 리스트 내포
# [식 for 변수 in 리스트]
# list(식 for 변수 in 리스트)

# 0 ~ 9
a = [i for i in range(10)]
print(a)

b = list(i for i in range(10))
print(b)

c = [i + 5 for i in range(10)]
print(c)

d = [i * 2 for i in range(10)]
print(d)
print()

# 리스트 표현식에서 if 문 사용
# [식 for 변수 in 리스트 if 조건문]
# list(식 for 변수 in 리스트 if 조건문)
a = [i for i in range(10) if i % 2 == 0]
print(a)

# if 문 여러번 사용
"""
[식 for 변수1 in 리스트1 if 조건식 1 for 변수2 in 리스트2 if 조건식2 ...]
"""
a = [i * j for i in range(2, 10) for j in range(1, 10)]
print(a)
print()

# 리스트에 map 사용하기
# 리스트의 요소를 지정된 함수로 처리해준다.
# list(map(함수, 리스트))
# tuple(map(함수, 튜플))
a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

a = list(map(int, a))
print(a)

b = list(map(str, range(10)))
print(b)
