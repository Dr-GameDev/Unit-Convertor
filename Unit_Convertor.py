# Unit Converter

def main():
    print("1: Temperature ", "2: Mass ", "3: Length")
    unit = int(input("What do you want to convert? 1, 2, or 3? "))

    if unit == 1:                      #TEMPERATURE OPTION
        temperature_choice = int(input("1: Celsius to Fahrenheit or 2: Fahrenheit to Celsius or 3: Kelvin to Celsius or 4: Kelvin to Fahrenheit "))
        if temperature_choice == 1:                                                        # Celsius to Fahrenheit
            value_input = float(input("Enter the value in C : "))
            converted_value = celsius_to_fahrenheit(value_input)
            print(f"{value_input} C is equal to {'{:.2f}'.format(round(converted_value, 2))} F ")
        elif temperature_choice == 2:                                                      # Fahrenheit to Celsius
            value_input = float(input("Enter the value in F : "))
            converted_value = fahrenheit_to_celsius(value_input)
            print(f"{value_input} F is equal to {'{:.2f}'.format(round(converted_value, 2))} C ")
        elif temperature_choice == 3:                                                      # Kelvin to Celsius
            value_input = float(input("Enter the value in K : "))
            converted_value = kelvin_to_celsius(value_input)
            print(f"{value_input} K is equal to {'{:.2f}'.format(round(converted_value, 2))} C ")
        elif temperature_choice == 4:                                                      # Kelvin to Fahrenheit
            value_input = float(input("Enter the value in K : "))
            converted_value = kelvin_to_fahrenheit(value_input)
            print(f"{value_input} K is equal to {'{:.2f}'.format(round(converted_value, 2))} F ")
        else:
            print("Option doesn't exist !")
    elif unit == 2:                    #MASS OPTION
        mass_choice = int(input("1: kg to lbs or 2: lbs to kg "))
        if mass_choice == 1:                                                               # Kilograms to Pounds
            value_input = float(input("Enter the value in kg: "))
            converted_value = kg_to_lbs(value_input)
            print(f"{value_input} kg is equal to {'{:.2f}'.format(round(converted_value, 2))} lbs")
        elif mass_choice == 2:                                                             # Pounds to Kilograms
            value_input = float(input("Enter the value in lbs: "))
            converted_value = lbs_to_kg(value_input)
            print(f"{value_input} lbs is equal to {'{:.2f}'.format(round(converted_value, 2))} kg")
        else:
            print("Invalid choice")
    elif unit == 3:                    #LENGTH OPTION
        print("At this stage of development, I can only convert centimetres and inches. Apologies for the inconvinience.")
        length_choice = int(input("1: cm to inch or 2: inch to cm "))
        if length_choice == 1:                                                              # cm to inches
            value_input = float(input("Enter value in cm: "))
            converted_value = cm_to_inch(value_input)
            print(f"{value_input} cm is equal to {'{:.2f}'.format(round(converted_value, 2))} inches")
        elif length_choice == 2:                                                            # inches to cm
            value_input = float(input("Enter value in inches: "))
            converted_value = inch_to_cm(value_input)
            print(f"{value_input} inches is equal to {'{:.2f}'.format(round(converted_value, 2))} cm")
        else:
            print("Invalid choice!!")
    else:
        print("Invalid choice")


def celsius_to_fahrenheit(value):
    return (value * 1.8) + 32


def fahrenheit_to_celsius(value):
    return (value - 32) * (1/1.8)


def kelvin_to_celsius(value):
    return value - 273.15


def kelvin_to_fahrenheit(value):
    return 1.8 * (value - 273) + 32


def kg_to_lbs(value):
    return value * 2.20462262


def lbs_to_kg(value):
    return value / 2.20462262


def cm_to_inch(value):
    return value / 2.54


def inch_to_cm(value):
    return value * 2.54


# Call the main function to start the program
main()
