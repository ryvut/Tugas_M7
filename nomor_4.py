import math

A = 4
B = 10
C = 4

root1 = (-B + math.sqrt(B**2 - 4*A*C)) / (2*A)
root2 = (-B - math.sqrt(B**2 - 4*A*C)) / (2*A)

turunan = []
for x in range(1, 11):
    f_prime = 2 * A * x + B
    turunan.append(f_prime)

print(f"root 1: {root1}")
print(f"root 2: {root2}")
print(f"f'(x): {turunan}")