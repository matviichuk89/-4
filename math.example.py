import math

x=float(input("Введіть x: "))
y=float(input("Введыть y: "))
z=float(input("Введіть z: "))
a=float(input("Введіть a: "))

L=6*a*x**3+math.sin(y)*math.cos(z)+math.tan(x+math.pi/3)

print(L)