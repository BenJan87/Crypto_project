# Python program to perform addition and multiplication
# on an elliptic curve

# We will use the secp256k1 curve for this example

# p is the prime number that defines the field GF(p)
p = 2**256 - 2**32 - 977

# a and b are the coefficients of the curve
a = 0
b = 7

# (x1, y1) and (x2, y2) are two points on the curve
x1 = 2
y1 = 3
x2 = 5
y2 = 7

# Calculate the slope of the line between the two points
if x1 == x2:
    # If the x-coordinates are the same, the points are vertical
    # and the slope is undefined. Instead, we use the point at
    # infinity as the result of the point addition.
    x3 = None
    y3 = None
else:
    # Calculate the slope of the line between the two points
    slope = (y2 - y1) / (x2 - x1)
    
    # Calculate the x-coordinate of the result of the point addition
    x3 = (slope**2 - x1 - x2) % p
    
    # Calculate the y-coordinate of the result of the point addition
    y3 = (slope * (x1 - x3) - y1) % p

# Print the result of the point addition
print(f'(x3, y3) = ({x3}, {y3})')

# Calculate the result of the point multiplication
# by adding the point to itself k times
k = 3
x4 = x3
y4 = y3
for i in range(k-1):
    x4, y4 = (x4+x3) % p, (y4+y3) % p

# Print the result of the point multiplication
print(f'k*(x3, y3) = ({x4}, {y4})')