"""
표준 입력으로 정수 두 개가 입력됩니다(첫 번째 입력 값의 범위는 10~1000, 두 번째 입력 값의 범위는 100~1000이며 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다). 다음 소스 코드에서 첫 번째 정수부터 두 번째 정수 사이의 소수(prime number)를 생성하는 제너레이터를 만드세요. 소수는 1과 자기자신만으로 나누어 떨어지는 1보다 큰 양의 정수입니다.
"""


def prime_number_generator(start, stop):
    while start < stop:
        isPrime = True
        for i in range(2, start):
            if start % i == 0:
                isPrime = False
                break
        if isPrime:
            yield start
        start += 1


# def prime_number(start, stop):
#     for n in range(start, stop):
#         is_prime = True
#         for i in range(2, n):
#             if n % i == 0:
#                 is_prime = False
#         if is_prime:
#             yield n


g = prime_number_generator(50, 100)
print(type(g))
for i in g:
    print(i, end=" ")
