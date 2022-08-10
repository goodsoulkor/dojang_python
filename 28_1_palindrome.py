# unit 28. 회문 판별과 N-gram

# 회문판별하기
# 회문 : 똑바로 읽어도 거꾸로 읽어도 같은 단어와 문장
# level, SOS, rotator...
# word = input()

# count = 0
# for i, s in enumerate(word):
#     if s == word[::-1][i]:
#         count += 1

# if count == len(word):
#     print(True)
# else:
#     print(False)

# word = input()

# is_palindrome = True
# for i in range(len(word) // 2):
#     if word[i] != word[-1 - i]:
#         is_palindrome = False
#         break

# print(is_palindrome)

# 시퀀스 뒤집기
# print(word == word[::-1])

# 리스트와 reversed 사용
# word = "level"
# print(list(word) == list(reversed(word)))

# join과 reversed 사용
# word = "level"
# print(word == "".join(reversed(word)))

# N-gram 만들기
# 문자열에서 N개의 연속된 요소를 추출하는 방법
# Hello -> 2-gram -> He, el, ll, lo
# text = "Hello"
# for i in range(len(text) - 1):
#     print(text[i], text[i + 1])

# 단어 단위 2-gram
# text = "this is python script"
# words = text.split()

# for i in range(len(words) - 1):
#     print(words[i], words[i + 1])

# zip으로 2-gram 만들기
# text = "hello"

# two_gram = zip(text, text[1:])
# for i in two_gram:
#     print(i[0], i[1])

# text = "this is python script"
# words = text.split()
# print(list(zip(words, words[1:])))

# zip과 리스트 표현식으로 N-gram 만들기
text = "hello"
print([text[i:] for i in range(3)])
print(list(zip(*[text[i:] for i in range(3)])))
