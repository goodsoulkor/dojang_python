# unit 38. try except 사용하기

# 예외처리 사용하기
"""
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
"""
# try:
#     x = int(input("나눌 숫자를 입력하세요: "))
#     y = 10 / x
#     print(y)
# except:  # 예외가 발생했을 때 실행됨
#     print("예외가 발생했습니다.")

# 특정 예외만 처리하기
"""
try:
    실행할 코드
except 예외이름:
    예외 발생 시 처리하는 코드
"""
y = [10, 20, 30]

try:
    index, x = map(int, input("인덱스와 나눌 숫자를 입력하세요: ").split())
    print(y[index] / x)
except ZeroDivisionError:  # 숫자를 0으로 나눌 때 실행됨
    print("0으로 나눌 수 없습니다.")
except IndexError:  # 범위를 벗어난 인덱스에 접근하면 실행됨
    print("잘못된 인덱스 입니다.")

# TODO 여기부터
