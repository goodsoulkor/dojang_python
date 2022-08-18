# unit 39. 반복 가능한 객체 알아보기

# print(dir([1, 2, 3]))
# print([1, 2, 3].__iter__())
# it = [1, 2, 3].__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# it = range(3).__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# for와 반복 가능한 객체
# __iter__()로 이터레이터를 얻고 __next__()로 하나씩 꺼낸다.

# 이터레이터 만들기
class Counter:
    def __init__(self, stop):
        self.current = 0  # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop = stop

    def __iter__(self):
        return self  # 현재 인스턴스를 반환

    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration


# for i in Counter(3):
#     print(i, end=" ")

# 이터레이터 언패킹
a, b, c = Counter(3)
# print(a, b, c)

# 인덱스로 접근할 수 있는 이터레이터 만들기
class Counter:
    def __init__(self, stop):
        self.stop = stop

    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError


# print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

# for i in Counter(3):
#     print(i, end=" ")

# __getitem__ 만 구현해도 이터레이터가 된다.

# iter, next 함수 활용하기
# iter: 객체의 __iter__ 메서드를 호출
# next: 객체의 __next__ 메서드를 호출

it = iter(range(3))
print(next(it))
print(next(it))
print(next(it))
print()

# iter
# 반복을 끝낼 값을 지정하면 특정 값이 나올 때 반복을 끝낸다.
# iter(호출가능한 객체, 반복을 끝낼 값)
import random

it = iter(lambda: random.randint(0, 5), 2)
# print(next(it))
# 2가 나오면 StopIteration 발생

# for i in iter(lambda: random.randint(0, 5), 2):
# print(i, end=" ")

# while True:
#     i = random.randint(0, 5)
#     if i == 2:
#         break
#     print(i, end=" ")

# next
# 기본값을 지정하면 반복이 끝나더라도 StopIteration이 발생하지 않고 기본값을 출력한다.
# next(반복가능한 객체, 기본값)
it = iter(range(3))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
print()
