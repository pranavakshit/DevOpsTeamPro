def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (m)."""
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    """Return the BMI category based on BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# User input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)
category = get_bmi_category(bmi)

# Display results
print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")
