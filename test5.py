def convert_temp():
    fahrenheit = float(input("The temperature in Fahrenheit is: "))
    celcius = convert_to_celcius(fahrenheit)
    print(f"The temperature in Fahrenheit: {fahrenheit}")
    print(f"The temperature in Celcius: {convert_to_celcius(fahrenheit)}")
    print(f"The temperature in Kelvin: {convert_to_kelvin(celcius)}")

def convert_to_celcius(fahrenheit):
    celcius = 5 / 9 * (fahrenheit - 32)
    return celcius

def convert_to_kelvin(celcius):
    kelvin = celcius + 273.15
    return kelvin

convert_temp()