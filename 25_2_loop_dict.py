# 반복문으로 키-값 출력하기
x = {"a": 10, "b": 20, "c": 30, "d": 40}
for i in x:
    print(i, end=" ")
print()

for key, value in x.items():
    print(key, value)
print()

for key, value in {"a": 10, "b": 20, "c": 30}.items():
    print(key, value)
print()

# 키만 출력하기
x = {"a": 10, "b": 20, "c": 30, "d": 40}
for key in x.keys():
    print(key)
print()

# 값만 출력하기
for value in x.values():
    print(value)
