print("Welcome to Rheo's Ohm's Law Calculator\nthis calculator assumes that all the values are in eiter ampere, volts, and ohms")
print("""Voltage - V
Current - I
Resistance - R""")
def initialization():
    calculator_type = input("What do you want to Calculate: V, I, or R ")
    if calculator_type.upper() == "V":
        voltage_calculator()
    elif calculator_type.upper() == "I":
        current_calculator()
    elif calculator_type.upper() == "R":
        resistance_calculator()
    else:
        print("Please choose from the options")
        initialization()

def voltage_calculator():
    try:
        current = float(input("Please enter your current reading "))
        resistance = float(input("Please enter resistance reading "))
        voltage = current*resistance
        print(f'The total voltage is {voltage}V')
    except (TypeError, ValueError) :
        print("Please enter the right values")
        voltage_calculator()
def current_calculator():
    try: 
        voltage = float(input("Please enter your voltage reading "))
        resistance = float(input("Please enter resistance reading "))
        current = voltage/resistance
        print(f'The total current is {current}amp')
    except (TypeError, ValueError) :
        print("Please enter the right values")
        current_calculator()
    except ZeroDivisionError:
        print("You cannot divide by zero")
        current_calculator()
def resistance_calculator():
    try: 
        voltage = float(input("Please enter your voltage reading "))
        current = float(input("Please enter current reading "))
        resistance = voltage/current
        print(f'The total current is {resistance}amp')
    except (TypeError, ValueError) :
        print("Please enter the right values")
        resistance_calculator()
    except ZeroDivisionError:
        print("You cannot divide by zero")
        
initialization()