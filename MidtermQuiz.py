
unit = input("Is this temperature in Celsius Fahrenheit or Kelvin: ")
temp = float(input("Enter the temperature: "))

if unit == "Celsius":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "Fahrenheit":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}°C")
elif unit == "Kelvin":
    temp = round((temp + 459.67)/1.8)
    print(f"The temperature in Celsius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")