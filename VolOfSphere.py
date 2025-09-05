import math

print("=== Sphere Volume Calculator ===")
print("Formula: V = (4/3) × π × r³")
print()

# Get radius input from user
# Using float() to handle decimal inputs
radius = float(input("Enter the radius of the sphere: "))

# Calculate volume using the formula: V = (4/3) * π * r³
# Using ** operator for exponentiation (r³) as required
volume = (4/3) * math.pi * (radius ** 3)

# Display the calculated volume
print()
print(f"Radius: {radius}")
print(f"Volume of the sphere: {volume:.4f}")
print()
print("Calculation steps:")
print(f"V = (4/3) × π × {radius}³")
print(f"V = (4/3) × {math.pi:.4f} × {radius**3:.4f}")
print(f"V = {volume:.4f}")