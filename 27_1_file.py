# unit 27 파일 사용하기

# 파일에 문자열 쓰기
# file = open("hello.txt", "w")
# file.write("hello world!")
# file.close()

# 파일에서 문자열 읽기
# file = open("hello.txt", "r")
# s = file.read()
# print(s)
# file.close()

# 자동으로 파일 객체 닫기
# with open("hello.txt", "r") as f:
#     s = f.read()
#     print(s)

# 반복문으로 문자열 여러 줄을 파일에 쓰기
# with open("hello.txt", "w") as f:
#     for i in range(3):
#         f.write("Hello world! {0}\n".format(i))

# 리스트에 들어있는 문자열 파일에 쓰기
# lines = ["Hello\n", "Python\n", "Dojang\n"]
# with open("hello.txt", "w") as f:
#     f.writelines(lines)

# 파일의 내용을 한 줄씩 리스트로 가져오기
# with open("hello.txt", "r") as f:
#     lines = f.readlines()
#     print(lines)

# 파일의 내용을 한 줄씩 읽기
# with open("hello.txt", "r") as f:
#     line = None
#     while line != "":
#         line = f.readline()
#         print(line.strip())

# for 반복문으로 파일의 내용을 줄 단위로 읽기
# with open("hello.txt", "r") as f:
#     for line in f:
#         print(line.strip())

# 객체를 파일에 저장하기
import pickle

name = "james"
age = 17
address = "Banpo Seocho, Seoul"
scores = {"korean": 90, "english": 95, "mathmatics": 85, "science": 82}

# with open("james.p", "wb") as f:
#     pickle.dump(name, f)
#     pickle.dump(age, f)
#     pickle.dump(address, f)
#     pickle.dump(scores, f)

# 파일에서 객체 읽기
# with open("james.p", "rb") as f:
#     name = pickle.load(f)
#     age = pickle.load(f)
#     address = pickle.load(f)
#     scores = pickle.load(f)
#     print(name)
#     print(age)
#     print(address)
#     print(scores)

# 파일 모드
"""
r : 읽기, w : 쓰기, a : 추가, x : 배타적 생성(파일이 있으면 에러, 없으면 생성)
rb : 바이너리 읽기, wb : 바이너리 쓰기
w+ : 읽기/쓰기(파일 내용 버림), r+ : 읽기/쓰기(파일 처음부터), a+ : 읽기/쓰기(파일 끝부터), x+ : 읽기/쓰기(파일 있으면 에러)
"""
