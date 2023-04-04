# Cube root

import math

print("Enter a Number: ", end="")
num = int(input())

response = math.pow(num, 1/3)
print("\nCube Root of %0.2f = %0.2f" %(num, response))
