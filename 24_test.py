import string

a = input()

b = a.split(" ")
count = 0
for i in b:
    if i.strip(string.punctuation) == "the":
        count += 1

print(count)
