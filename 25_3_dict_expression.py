# 딕셔너리 표현식 사용
# {키: 값 for 키, 값 in 딕셔너리}
# dict({키: 값 for 키, 값 in 딕셔너리})
keys = ["a", "b", "c", "d"]
x = {key: value for key, value in dict.fromkeys(keys).items()}
print(x)

y = {key: 0 for key in dict.fromkeys(["a", "b", "c", "d"]).keys()}
print(y)
z = {value: 0 for value in {"a": 10, "b": 20, "c": 30}.values()}
print(z)

j = {value: key for key, value in {"a": 10, "b": 20, "c": 30}.items()}
print(j)
print()

# 표현식에서 if 조건문 사용하기 - 삭제 시 반복문 사용하면 오류 발생
# x = {"a": 10, "b": 20, "c": 30, "d": 40}
# for key, value in x.items():
#     if value == 20:
#         del x[key]
# print(x)
x = {"a": 10, "b": 20, "c": 30, "d": 40}
x = {key: value for key, value in x.items() if value != 20}
print(x)
