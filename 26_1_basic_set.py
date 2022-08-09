# unit 26. 세트

# 세트 만들기
# 세트 = {val1, val2, val3}
fruits = {"strawberry", "grape", "orange"}
print(fruits)

# 순서가 없고 중복을 허용하지 않는다.
fruits = {"strawberry", "orange", "orange"}
print(fruits)
print()
# 순서가 없기 때문에 인덱싱, 슬라이싱 할 수 없다.

# 세트에 특정 값이 있는지 확인
fruits = {"strawberry", "grape", "orange", "pineapple", "cherry"}
print("orange" in fruits)
print("peach" not in fruits)
print()

# set을 사용하여 세트 만들기
# set(반복 가능한 객체)
a = set("apple")
print(a)
b = set(range(5))
print(b)
c = set()
print(c)
# 세트 안에 세트를 넣을 수 없다.

# 내용을 변경할 수 없는 세트 - frozenset
a = frozenset(range(10))  # 요소를 추가하거나 삭제하는 연산, 메서드는 사용할 수 없다.
print(a)
# 중첩을 하기 위해 frozenset을 사용한다.
a = frozenset({frozenset({1, 2}), frozenset({3, 4})})
print(a)
print()

# 집합 연산
# 합집합 |, set.union
a = {1, 2, 3, 4}
b = {5, 6, 7, 8}
print(a | b)
print(set.union(a, b))
print()

# 교집합 &, set.intersection
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)
print(set.intersection(a, b))
print()

# 차집합 -, set.difference
print(a - b)
print(set.difference(a, b))
print()

# 대칭차집합 ^, set.symmetric_difference
print(a ^ b)
print(set.symmetric_difference(a, b))
print()

# 집합 연산 후 할당 연산자 사용하기
a = {1, 2, 3, 4}
a |= {5}
print(a)

b = {1, 2, 3, 4}
b.update({5})
print(b)
print()

# 겹치는 요소만 저장
a = {1, 2, 3, 4}
a &= {0, 1, 2, 3, 4}
print(a)
b = {1, 2, 3, 4}
b.intersection_update({0, 1, 2, 3, 4})
print(b)
print()

# 현재 세트에서 다른 세트 빼기
a = {1, 2, 3, 4}
a -= {3}
print(a)
b = {1, 2, 3, 4}
b.difference_update({3})
print(b)
print()

# 현재 세트와 다른 세트에서 겹치지 않는 요소만 저장
a = {1, 2, 3, 4}
a ^= {3, 4, 5, 6}
print(a)
b = {1, 2, 3, 4}
b.symmetric_difference_update({3, 4, 5, 6})
print(b)
print()

# 부분 집합과 상위집합 확인하기
# 부분 집합 - 같을 때도 참
a = {1, 2, 3, 4}
print(a <= {1, 2, 3, 4})
print(a.issubset({1, 2, 3, 4, 5}))

# 진부분집합 - 같지 않을 때 참
a = {1, 2, 3, 4}
print(a < {1, 2, 3, 4, 5})

# 상위집합 - 같을 때도 참
a = {1, 2, 3, 4}
print(a >= {1, 2, 3, 4})
print(a.issuperset({1, 2, 3, 4}))

# 진상위집합 - 같지 않을 때 참
a = {1, 2, 3, 4}
print(a > {1, 2, 3})
print()

# 세트가 같은지 다른지 확인하기
a = {1, 2, 3, 4}
print(a == {1, 2, 3, 4})
print(a == {4, 2, 1, 3})

b = {1, 2, 3, 4}
print(b != {1, 2, 3})
print()

# 세트가 겹치지 않는지 확인
a = {1, 2, 3, 4}
print(a.isdisjoint({5, 6, 7, 8}))
print(a.isdisjoint({3, 4, 5, 6}))  # 3, 4가 겹침
