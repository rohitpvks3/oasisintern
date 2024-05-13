def calculate_bmi(weight, height):
    
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    """
    Classify the BMI into categories based on predefined ranges.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def convert_height_to_meters(height, unit):
    """
    Convert height to meters based on the specified unit.
    """
    if unit.lower() == "m":
        return height
    elif unit.lower() == "cm":
        return height / 100
    elif unit.lower() == "ft":
        return height * 0.3048  # 1 foot = 0.3048 meters
    elif unit.lower() == "in":
        return height * 0.0254  # 1 inch = 0.0254 meters
    else:
        raise ValueError("Invalid height unit. Please use 'm', 'cm', 'ft', or 'in'.")

def main():
    print("Welcome to the BMI Calculator!")
    print("Please enter your weight (in kilograms) and height.")

    try:
        weight = float(input("Enter your weight in kilograms: "))

        height_unit = input("Enter the unit of height (m/cm/ft/in): ")
        height_value = float(input(f"Enter your height in {height_unit}: "))

        height_in_meters = convert_height_to_meters(height_value, height_unit)

        if weight <= 0 or height_value <= 0:
            print("Error: Weight and height must be positive values.")
            return

        bmi = calculate_bmi(weight, height_in_meters)
        category = classify_bmi(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
