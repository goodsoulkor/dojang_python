# 딕셔너리 안에서 딕셔너리 사용

terrestrial_planet = {
    "Mercury": {"mean_radius": 2439.7, "mass": 3.3022e23, "orbital_period": 87.969},
    "Venus": {"mean_radius": 2439.7, "mass": 3.3022e23, "orbital_period": 87.969},
    "Earth": {"mean_radius": 2439.7, "mass": 3.3022e23, "orbital_period": 87.969},
}

print(terrestrial_planet["Venus"]["mean_radius"])

# 딕셔너리의 할당과 복사
x = {"a": 10, "b": 20, "c": 30}
y = x
print(x is y)
y["a"] = 99
print(x)
print(y)
print()

# 복사
x = {"a": 10, "b": 20, "c": 30}
y = x.copy()
print(x is y)
print(x == y)
y["a"] = 99
print(x)
print(y)
print()

# 중첩 딕셔너리의 할당과 복사
x = {"a": {"python": "2.7"}, "b": {"python": "3.6"}}
y = x.copy()
y["a"]["python"] = "2.7.15"
print(x)
print(y)

# 중첩 딕셔너리를 복사하려면 deepcopy 사용
import copy

x = {"a": {"python": "2.7"}, "b": {"python": "3.6"}}
y = copy.deepcopy(x)
y["a"]["python"] = "2.7.15"
print(x)
print(y)
