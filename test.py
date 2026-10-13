Первое задание!!!

import math

f,n = math.pi/4, 6

arg_a = f*n
a = math.tan(arg_a)
arg_y2 = (math.pi*n)/(2*f)


y1 = 5*a**(-2)
y2 = abs(math.tan(arg_y2))

print(f"a = {a:.5e}")
print(f"y1 = {y1:.5e}")
print(f"y2 = {y2:.5f}")

try:
    y3 = (math.exp(5*a)) ** 0.5
    y = y1-y2*y3
    print(f"y = {y}")
except OverflowError:
    print("ОШИБКА")








