import math

# TASK 10 - BMI Health Information

# Ask for the person's name and reject blank input.
while True:
    name = input("Name: ").strip()
    if name:
        break
    print("Name cannot be blank. Please try again.")

# Ask for a finite, non-negative weight.
while True:
    try:
        weight = float(input("Weight in kilograms: "))
        if not math.isfinite(weight):
            print("Please enter a normal number, such as 60 or 60.5.")
        elif weight < 0:
            print("Weight cannot be negative. Please try again.")
        else:
            break
    except ValueError:
        print("Please enter a valid number, such as 60 or 60.5.")

# Ask for a finite height greater than zero.
while True:
    try:
        height = float(input("Height in meters: "))
        if not math.isfinite(height):
            print("Please enter a normal number, such as 1.70.")
        elif height <= 0:
            print("Height must be greater than zero. Please try again.")
        else:
            break
    except ValueError:
        print("Please enter a valid number, such as 1.70.")

# Calculate BMI.
bmi = weight / (height * height)

# Display the BMI report.
print()
print("=" * 32)
print("          BMI REPORT")
print("=" * 32)
print(f"Name: {name}")
print(f"Weight: {weight:g} kg")
print(f"Height: {height:.2f} m")
print()
print(f"BMI: {bmi:.2f}")
print("=" * 32)