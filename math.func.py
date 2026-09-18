import math

def func1(x):
    y=2.7*math.log10(abs(math.sin(math.sqrt(x))))-(8/abs(math.sqrt(x)+math.cbrt(x))+0.02)
    return (y)

x=float(input("Введіть x: "))
y=func1(x)

print(y)