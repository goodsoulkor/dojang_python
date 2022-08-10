# unit 31. 함수에서 재귀 호출 사용
# 함수에서 자기 자신을 호출하는 방식을 재귀호출 이라 한다.

# 사용
# def hello():
#     print("Hello, world!")
#     hello()


# hello()
# 최대 재귀호출 깊이(1000)를 넘어가면 오류 발생

# 재귀호출에 종료 조건 만들기
def hello(count):
    if count == 0:
        return
    print("Hello, world!", count)

    count -= 1
    hello(count)


# hello(5)

# 재귀호출로 팩토리얼 구현
# 팩토리얼 : 1부터 n 까지 양의 정수를 차례대로 곱한 값으로 ! 기호로 표현
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(4))
