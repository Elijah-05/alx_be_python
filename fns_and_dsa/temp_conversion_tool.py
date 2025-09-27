
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit} is : {celsius}")
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius} is {fahrenheit}")
    return fahrenheit

def main():
    try:
        temp_str = input("Enter the temperature to convert: ").strip()
        temp_float = float(temp_str)
    
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        print(f"find the temp_float: {temp_str}")
        convert_to_fahrenheit(temp_float)
    elif unit == "F":
        print(f"find the temp_float: {temp_str}")
        convert_to_celsius(temp_float)
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()