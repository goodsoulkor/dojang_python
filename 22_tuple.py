# 요소의 정보를 구하는 메서드만 사용가능
a = (38, 21, 53, 62, 19, 53)
print(a.index(21))

a = (10, 20, 30, 15, 20, 40)
print(a.count(20))

# 튜플 표현식
a = tuple(i for i in range(10) if i % 2 == 0)
print(a)

a = (1.2, 2.5, 3.7, 4.6)
a = tuple(map(int, a))
print(a)

a = (38, 21, 53, 62, 19)
print(min(a))
print(max(a))
print(sum(a))
