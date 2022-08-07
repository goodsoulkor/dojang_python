# unit24. 문자열 조작하기

# 문자열 바꾸기 - replace
# replace("바꿀문자열", "새 문자열")
print("hello world!".replace("world", "Python"))
print()

s = "hello world"
s = s.replace("hello", "python")
print(s)
print()

# 문자 바꾸기 - str.maketrans / translate
table = str.maketrans("aeiou", "12345")
print("apple".translate(table))
print()

# 문자열 분리하기 - split
print("apple pear grape pineapple orange".split())
print()

# 구분자 문자열과 문자열 리스트 연결하기 - join(리스트)
print(" ".join(["apple", "pear", "grape"]))
print()

print("-".join(["apple", "orange", "grape"]))
print()

# 소문자를 대문자로 바꾸기 - upper()
print("python".upper())
print()

# 대문자를 소문자로 바꾸기 - lower()
print("PYTHON".lower())
print()

# 왼쪽 공백 삭제하기 - lstrip()
print("  python".lstrip())
print()

# 오른쪽 공백 삭제하기 - rstrip()
print("python  ".rstrip())
print()

# 양쪽 공백 삭제하기 - strip()
print("  python  ".strip())
print()

# 왼쪽의 특정 문자 삭제하기 - lstrip("삭제할문자들")
print(",python.".lstrip(",."))
print()

# 오른쪽의 특정 문자 삭제하기 - rstrip("삭제할문자들")
print(",python.".rstrip(",."))
print()

# 양쪽의 특정 문자 삭제하기 - strip("삭제할문자들")
print(", python.".strip(",."))
print()

# 구두점을 간단하게 삭제하기
import string

print(string.punctuation)
print()
print(", python.".strip(string.punctuation))
print(", python.".strip(string.punctuation + " "))
print(", python.".strip(string.punctuation).strip())
print()

# 문자열 왼쪽 정렬하기 - ljust(길이)
print("python".ljust(10))
# 문자열을 오른쪽 정렬하기 - rjust(길이)
print("python".rjust(10))
# 문자열을 가운데로 정렬하기 - center(길이)
print("python".center(10))
# 남는 공간이 홀수이면 왼쪽에 한 칸이 더 들어간다.
print("python".center(11))
print()

# 메서드 체이닝 - 메서드를 줄줄이 연결한다.
print("python".rjust(10).upper())
print()

# 문자열 왼쪽에 0 채우기 - zfill(길이)
print("35".zfill(4))
print("3.5".zfill(6))
print("hello".zfill(10))
print()

# 문자열 위치 찾기 - find("찾을문자열")
print("apple pineaplle".find("pl"))
print("apple pineapple".find("xy"))
print()

# 오른쪽에서 부터 문자열 찾기 - rfind("찾을 문자열")
print("apple pineapple".rfind("pl"))
print("apple pineapple".rfind("xy"))
print()

# 문자열 위치찾기 2 - index, rindex
print("apple pineapple".index("pl"))
print("apple pineapple".rindex("pl"))
print()

# 문자열 개수 세기 - count
print("apple pineapple".count("pl"))
