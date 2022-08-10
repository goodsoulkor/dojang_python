# unit 30. 함수에서 위치 인수와 키워드 인수 사용

# 위치 인수와 리스트 언패킹
def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)


# print_numbers(1, 2, 3)

# 언패킹
# x = [1, 2, 3]
# print_numbers(*x)
# print_numbers(*[1, 2, 3])

# 가변 인수 함수 만들기
def print_numbers(*args):
    print(args)
    for arg in args:
        print(arg)


print_numbers(1)
print_numbers(1, 2, 3, 4)
print()

x = [10]
print_numbers(*x)
y = [1, 2, 3, 4]
print_numbers(*y)
print_numbers(y)
print()

# 고정 인수와 가변인수 함께 사용
# 고정 매개변수를 먼저 지정
def print_numbers(a, *args):
    print(a)
    print(args)


print_numbers(1)
print_numbers(1, 10, 20)
print_numbers(*[10, 20, 30])
print()

# 키워드 인수
def personal_info(name, age, address):
    print("이름:", name)
    print("나이:", age)
    print("주소:", address)


personal_info(name="goodsoul", age=40, address="seoul")
print()

# 키워드 인수와 딕셔너리 언패킹
def personal_info(name, age, address):
    print("이름:", name)
    print("나이:", age)
    print("주소:", address)


x = {"name": "goodsoul", "age": 40, "address": "seoul"}
personal_info(**x)
print()

# 딕셔너리는 키-값 형태로 값이 저장되어 있기 때문에 ** 두개로 사용한다.
personal_info(*x)
print()

# 키워드 인수를 사용하는 가변 인수 함수 만들기
def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ": ", arg, sep="")


personal_info(name="goodsoul")
personal_info(name="goodsoul", age=40, address="seoul")
x = {"name": "goodsoul"}
personal_info(**x)
print()


def personal_info(**kwargs):
    if "name" in kwargs:
        print("name: ", kwargs["name"])
    if "age" in kwargs:
        print("age: ", kwargs["age"])
    if "address" in kwargs:
        print("address: ", kwargs["address"])


# 위치인수와 키워드 인수 함께 사용
def custom_print(*args, **kwargs):
    print(*args, **kwargs)


custom_print(1, 2, 3, sep=":", end="")
print()

# 매개변수에 초기값 지정하기
def personal_info(name, age, address=None):
    print("name: ", name)
    print("age: ", age)
    print("address: ", address)


personal_info("goodsoul", 40)
print()
personal_info("goodsoul", 40, "seoul")
print()

# 초기값이 지정된 매개변수의 위치
# 초기값이 지정된 매개변수는 항상 뒤에 와야한다.
