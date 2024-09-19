print("Welcome to Rheo's temperature converter\nthis converts Fahrenheit to Celsius and vice versa")
def temperature_Converter():
    try:
        user_temperature_value = input("Enter the temperature that you want to convert. e.g. 34\n")
        if user_temperature_value.isalpha():
            print("please only enter intigers")
            temperature_Converter()
        else:
            user_temperature_type = input("""Enter your corresponding conversion type (CTF or FTC)
from Celsius to Fahrenheit - CTF
from Fahrenheit to Celsius - FTC
""" )
            temperture_value = float(user_temperature_value)
            if user_temperature_type.upper() == "CTF":
                result = (temperture_value*1.8)+32
                print(f"The resulting temperature is {result}°F")
            elif user_temperature_type.upper() == "FTC":
                result = (temperture_value - 32)/1.8
                print(f"The resulting temperature is {result}°C")
            else:
                print("Please select between FTC or CTF")
                temperature_Converter()
    except TypeError:
        print("Please follow the needed format")
    except  ValueError:
        print("Please follow the given format")

temperature_Converter()