def convert_temperature(temp, unit):
    if unit == 'F':
        converted = (temp - 32) * 5/9
        return round(converted, 2), 'Celsius'
    elif unit == 'C':
        converted = (temp * 9/5) + 32
        return round(converted, 2), 'Fahrenheit'
    else:
        return "Invalid unit. Use 'F' for Fahrenheit or 'C' for Celsius.", None

# User selects conversion type
print("Choose conversion type:")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
choice = input("Enter 1 or 2: ")

if choice == '1':
    unit = 'F'
    print("You selected: Fahrenheit to Celsius")
elif choice == '2':
    unit = 'C'
    print("You selected: Celsius to Fahrenheit")
else:
    print("Invalid choice. Please enter 1 or 2.")
    exit()

# User input
temp = float(input(f"Enter the temperature in {unit}: "))

# Convert and display result
converted_temp, converted_unit = convert_temperature(temp, unit)
print(f"{temp}° {unit} is Equal to {converted_temp}° {converted_unit}.")
