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
# y = [10, 20, 30]

# try:
#     index, x = map(int, input("인덱스와 나눌 숫자를 입력하세요: ").split())
#     print(y[index] / x)
# except ZeroDivisionError:  # 숫자를 0으로 나눌 때 실행됨
#     print("0으로 나눌 수 없습니다.")
# except IndexError:  # 범위를 벗어난 인덱스에 접근하면 실행됨
#     print("잘못된 인덱스 입니다.")


# 예외의 에러 메시지 받아오기
# y = [10, 20, 30]

# try:
#     index, x = map(int, input("인덱스와 나눌 숫자를 입력하세요: ").split())
#     print(y[index] / x)
# except ZeroDivisionError as e:
#     print("숫자를 0으로 나눌 수 없습니다.", e)
# except IndexError as e:
#     print("잘못된 인덱스 입니다.", e)

# else, finally 사용
# else: 예외가 발생하지 않을 때 실행하는 코드
# try:
#     x = int(input("나눌 숫자 입력: "))
#     y = 10 / x
# except ZeroDivisionError:
#     print("숫자를 0으로 나눌 수 없습니다.")
# else:
#     print(y)

# finally: 예외와는 상관 없이 항상 코드 실행하기
# try:
#     x = int(input("나눌 숫자 입력: "))
#     y = 10 / x
# except ZeroDivisionError as e:
#     print(e)
# else:
#     print(y)
# finally:
#     print("code end")

# 예외 발생 시키기
# 3의 배수가 아니면 에러 발생시키기
# try:
#     x = int(input("3의 배수: "))
#     if x % 3 != 0:
#         raise Exception("3의 배수가 아님")
#     print(x)
# except Exception as e:
#     print("예외발생:", e)

# raise의 처리 과정
# def three_multiple():
#     x = int(input("3의 배수: "))
#     if x % 3 != 0:
#         raise Exception("3의 배수가 아님")
#     print(x)


# try:
#     three_multiple()
# except Exception as e:
#     print("예외발생:", e)

# except가 없는 상태에서 raise 발생 시 except가 나올 때 까지 상위 코드 블록으로 올라감

# 현재 예외를 다시 발생 시키기
# def three_multiple():
#     try:
#         x = int(input("3 multiple: "))
#         if x % 3 != 0:
#             raise Exception("not 3 multiple")
#         print(x)
#     except Exception as e:  # 함수 안에서 예외 처리
#         print("error in function three_multiple", e)
#         raise  # 현재 예외를 다시 발생 시켜 상위 코드로 넘김


# try:
#     three_multiple()
# except Exception as e:
#     print("error in code", e)

# assert로 예외 발생
# 지정된 조건식이 거짓일 때 AssertionError 발생
# x = int(input("3 multiple: "))
# assert x % 3 == 0, "not 3 multiple"  # 3의 배수가 아니면 예외
# print(x)

# 예외 만들기
class NotThreeMultipleError(Exception):  # Exception을 상속받아 새로운 예외 생성
    def __init__(self):
        super().__init__("not 3 multiple")


def three_multiple():
    try:
        x = int(input("3 multiple: "))
        if x % 3 != 0:
            raise NotThreeMultipleError
        print(x)
    except Exception as e:
        print("error in code:", e)


three_multiple()
