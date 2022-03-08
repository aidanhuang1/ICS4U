import glob
import random

s = "#pink#family#swag"
s = s.split('#')
dict = {"1": "no", "2": "yes"}
print(s[1])

for key in dict:
    print(key, dict[key])


a = "a.b.c.d.e.f.g"
a = a.strip().split('.', 2)
print(a)

print(random.randint(99,100))

t = "abcedfg"
print(t[:-1])
s = glob.glob("*")
print(s)