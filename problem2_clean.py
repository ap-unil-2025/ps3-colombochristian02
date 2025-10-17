"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""


def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C * 9/5) + 32
    """
    return (celsius * 9/5) + 32



def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) * 5/9
    """
    return (fahrenheit - 32) * 5/9


def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
    print("Temperature Converter")
    print("-" * 30)

    temperature = float(input("Enter the temperature: "))
    unit = input("Enter unit of temperature, either C or F: ").strip().upper()

    if unit == "C":
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result:.2f}°F")
    elif unit == "F":
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is {result:.2f}°C")
    else:
        print("The unit isn't valid!")


# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()
    