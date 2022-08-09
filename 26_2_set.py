# set 조작하기

# 요소 추가
a = {1, 2, 3}
a.add(5)
print(a)
print()

# 특정 요소 삭제
a.remove(3)
print(a)
print()

# discard(요소)는 특정 요소를 삭제하고 요소가 없으면 넘어간다.
a = {1, 2, 3, 4, 5}
a.discard(3)
print(a)
a.discard(3)
print(a)
print()

# 임의의 요소 삭제
a = {1, 2, 3, 4}
print(a.pop())
print(a)
print()

# 모든 요소 삭제
a.clear()
print(a)
print()

# 요소 개수 구하기
a = {1, 2, 3, 4}
print(len(a))
print()

# 할당
a = {1, 2, 3}
b = a
print(a is b)
b.add(4)
print(a, b)
print()

# 복사
a = {1, 2, 3}
b = a.copy()
print(a is b)
print(a == b)
b.add(4)
print(a, b)
print()

# 반복문으로 모두 출력하기
a = {1, 2, 3, 4}
for i in a:
    print(i)
print()

# set 표현식
a = {i for i in "apple"}
print(a)
print()

# set 표현식에 if 조건문 사용
a = {i for i in "pineapple" if i not in "apl"}
print(a)
