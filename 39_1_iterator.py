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
print(a, b, c)

# TODO 39.3 진행
