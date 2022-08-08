# unit 25 딕셔너리 응용하기

# 딕셔너리에 키-값 쌍 추가하기
# setdefault: 키-값 쌍 추가 / update: 키의 값 수정, 키가 없으면 키-값 쌍 추가
x = {"a": 10, "b": 20, "c": 30, "d": 40}
# 값 없이 사용하면 None을 추가
x.setdefault("e")
print(x)
print()

# setdefaul(키, 값)으로 사용하면 저장 후 해당 값을 반환한다.
print(x.setdefault("f", 100))
print(x)
print()

# update로 키, 값 수정하기
x = {"a": 10, "b": 20, "c": 30, "d": 40}
x.update(a=90)
print(x)
# 키가 없으면 추가
x.update(e=50)
print(x)
# 여러개 추가
x.update(a=900, f=60)
print(x)
# 키가 문자열 일때만 사용가능
# 키가 숫자인 경우 update(딕셔너리)로 사용
y = {1: "one", 2: "two"}
y.update({1: "ONE", 3: "THREE"})
print(y)
print()

# 리스트와 튜플 이용
y.update([[2, "TWO"], [4, "FOUR"]])
print(y)

# update(반복가능한 객체)
y.update(zip([1, 2], ["one", "two"]))
print(y)
print()

# 키-값 삭제하기
# pop(키) 특정 키-값을 삭제 후 삭제한 값을 반환
x = {"a": 10, "b": 20, "c": 30, "d": 40}
print(x.pop("a"))
print(x)

# pop(키, 기본값) 키가 있는 경우 키-값을 삭제하고 키가 없는 경우 기본값을 반환
print(x.pop("z", 0))
print()

# del x[키]
x = {"a": 10, "b": 20, "c": 30, "d": 40}
del x["a"]
print(x)
print()

# 임의의 키-값 삭제하기
# popitem() 임의의 키-값을 삭제 후 튜플로 반환
# 3.6 이상에서는 마지막 키-값
# 3.5 이하에서는 임의의 키-값
x = {"a": 10, "b": 20, "c": 30, "d": 40}
print(x.popitem())
print(x)
print()

# 모든 키-값 삭제
# clear()
x = {"a": 10, "b": 20, "c": 30, "d": 40}
x.clear()
print(x)
print()

# 키의 값 가져오기
# get(키)
x = {"a": 10, "b": 20, "c": 30, "d": 40}
print(x.get("a"))
# get(키, 기본값) - 키가 있으면 해당 값, 없으면 기본값
print(x.get("z", 0))
print()

# 키-값 모두 가져오기
# items : 키-값 쌍을 모두 가져오기
# keys : 키 모두 가져오기
# values : 값 모두 가져오기
x = {"a": 10, "b": 20, "c": 30, "d": 40}
print(x.items())
print(x.keys())
print(x.values())
print()

# 리스트와 튜플로 딕셔너리 만들기
keys = ["a", "b", "c", "d"]  # or tuple
x = dict.fromkeys(keys)
print(x)
y = dict.fromkeys(keys, 100)
print(y)
