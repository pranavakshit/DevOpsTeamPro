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

def run_tests():
    """Run test cases divided between Pranav and Kushagra."""
    
    # Pranav's Test Cases
    pranav_tests = [
        (50, 1.6, 19.53, "Normal weight"),  # Normal weight
        (45, 1.7, 15.57, "Underweight"),    # Underweight
        (100, 1.8, 30.86, "Obese")          # Obese
    ]

    
  # Running Pranav's test cases
    print("\nRunning Pranav's test cases:")
    for weight, height, expected_bmi, expected_category in pranav_tests:
        bmi = round(calculate_bmi(weight, height), 2)
        category = get_bmi_category(bmi)
        assert bmi == expected_bmi, f"Failed: Expected BMI {expected_bmi}, got {bmi}"
        assert category == expected_category, f"Failed: Expected category {expected_category}, got {category}"
        print(f"✅ Passed for weight={weight}, height={height}")

run_tests()


# User input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)
category = get_bmi_category(bmi)

# Display results
print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")
