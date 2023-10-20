a, b, c = [float(v) for v in input().split()]

PI = 3.14159

triangle_area = a * c / 2
circle_area = PI * c**2
trapezoid_area = (a + b) * c / 2
square_area = b**2
retangle_area = a * b

print(f"TRIANGULO: {triangle_area:.3f}")
print(f"CIRCULO: {circle_area:.3f}")
print(f"TRAPEZIO: {trapezoid_area:.3f}")
print(f"QUADRADO: {square_area:.3f}")
print(f"RETANGULO: {retangle_area:.3f}")
