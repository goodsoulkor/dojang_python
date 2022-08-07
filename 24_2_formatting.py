# 24.2 문자열 서식 지정자와 포매팅 사용하기

# 서식 지정자
print("I am %s." % "james")
name = "maria"
print("I am %s." % name)
print()

# 서식 지정자로 숫자 넣기 - %d
print("I am %d years old." % 20)
print()

# 서식 지정자로 소수점 표현하 - %f %.자리수f
print("%f" % 2.3)
print("%.2f" % 2.3)
print("%.3f" % 2.3)
print()

# 서식 지정자로 문자열 정렬하기
print("%10s" % "python")

# 왼쪽 정렬
print("%-10s" % "python")
print()

# 서식 자정자로 문자열 안에 값 여러개 넣기 - "%d %s" % (숫자, "문자열")
print("Today is %d %s." % (3, "April"))
print()

# format 메서드 사용하기
print("Hello, {0}".format("world!"))
print("Hello, {0}".format(100))
print()

# format 메서드로 값 여러 개 넣기
print("Hello, {0} {2} {1}".format("Python", "Script", 3.6))
print()

# format 메서드로 같은 값을 여러개 넣기
print("{0} {0} {1} {1}".format("python", "script"))

# format 메서드에서 인덱스 생략하기
print("Hello, {} {} {}".format("python", "script", 3.6))
print()

# format 메서드에서 인덱스 대신 이름 지정하기
print("Hello, {language} {version}".format(language="python", version=3.6))
print()

# 문자열 포매팅 변수를 그대로 사용하기
language = "Python"
version = 3.6
print(f"Hello, {language} {version}")
print()

# 중괄호 출려하기 - {{ }}
print("{{ {0} }}".format("python"))
print()

# format 메서드로 정렬하기 - "{인덱서:<길이}".format(값)
print("{0:<10}".format("python"))
print("{0:>10}".format("python"))
print("{:>10}".format("python"))
print()

# 숫자 개수 맞추기 - "%0개수d" % 숫자 / "{인덱스:0개수d}".format(숫자)
print("%03d" % 1)
print("{0:03d}".format(35))
print("%08.2f" % 3.6)
print("{0:08.2f}".format(150.37))
print()

# 채우기와 정렬 조합
print("{0:0<10}".format(15))
print("{0:0>10}".format(15))
print("{0:0>10.2f}".format(15))
print("{0: >10}".format(15))
print("{0:>10}".format(15))
print("{0:x>10}".format(15))
print()

# 금액에 천단위 콤마 넣기
print(format(1493500, ","))
print("%20s" % format(1493500, ","))
print("{0:,}".format(1493500))
print("{0:>20,}".format(1493500))
print("{0:0>20,}".format(1493500))
