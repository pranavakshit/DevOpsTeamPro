def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (m)."""
    bmi = weight / (height ** 2)
    return bmi


# User input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)
category = get_bmi_category(bmi)

# Display results
print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")
