# Supported Conversions: m to km, l to ml, oz to l, c to f, c to k, in to ft, cm to in, mi to m, lb to kg

def meters_to_km(meters):
    """Returns the value of meters divided by 1000"""
    return meters / 1000


def km_to_meters(km):
    """Returns the value of kilometers multiplied by 1000"""
    return km * 1000


def liters_to_ml(liters):
    """Returns the value of liters multiplied by 1000"""
    return liters * 1000


def ml_to_liters(ml):
    """Returns the value of milliliters divided by 1000"""
    return ml / 1000


def oz_to_liters(oz):
    """Returns the value of ounces divided by 33.814"""
    return oz / 33.814


def liters_to_oz(liters):
    """Returns the value of liters multiplied by 33.814"""
    return liters * 33.814


def cel_to_fahren(celsius):
    """Returns the value of degree Celsius converted to degree Fahrenheit"""
    return (celsius * 9 / 5) + 32


def fahren_to_cel(fahrenheit):
    """Returns the value of degree Fahrenheit converted to degree Celsius"""
    return (fahrenheit - 32) * 9 / 5


def cel_to_kel(celsius):
    """Returns the value of degree Celsius converted to Kelvin"""
    return celsius + 273.15


def kel_to_cel(kelvin):
    """Returns the value of Kelvin to degree Celsius"""
    return kelvin - 273.15


def inch_to_ft(inch):
    """Returns the value of inches divided by 12"""
    return inch / 12


def ft_to_inch(feet):
    """Returns the value of feet multiplied by 12"""
    return feet * 12


def cm_to_inch(centimeters):
    """Returns the value of centimeters divided by 2.54"""
    return centimeters / 2.54


def inch_to_cm(inch):
    """Returns the value of inches multiplied by 2.54"""
    return inch * 2.54


def miles_to_meters(mile):
    """Returns the value of miles multiplied by 1609.34"""
    return mile * 1609.34


def meters_to_miles(meters):
    """Returns the value of meters divided by 1609.34"""
    return meters / 1609.34


def lb_to_kg(pounds):
    """Returns the value of pounds divided by 2.205"""
    return pounds / 2.205


def kg_to_lb(kilograms):
    """Returns the value of kilograms multiplied by 2.205"""
    return kilograms * 2.205


conversion_dict = {
    "meters to kilometers": meters_to_km,
    "kilometers to meters": km_to_meters,
    "liters to milliliters": liters_to_ml,
    "milliliters to liters": ml_to_liters,
    "ounces to liters": oz_to_liters,
    "liters to ounces": liters_to_oz,
    "celsius to fahrenheit": cel_to_fahren,
    "fahrenheit to celsius": fahren_to_cel,
    "celsius to kelvin": cel_to_kel,
    "kelvin to celsius": kel_to_cel,
    "inches to feet": inch_to_ft,
    "feet to inches": ft_to_inch,
    "centimeters to inches": cm_to_inch,
    "inches to centimeters": inch_to_cm,
    "miles to meters": miles_to_meters,
    "meters to miles": meters_to_miles,
    "pounds to kilograms": lb_to_kg,
    "kilograms to pounds": kg_to_lb
}

# user input value


def convert_from_user():
    print("Supported Conversions (convert to and from): meters to kilometers, liters to milliliters, ounces to liters, "
          "Celsius to Fahrenheit, Celsius to Kelvin, inches to feet \n centimeters to inches, miles to meters, "
          "pounds to kilograms")
    which_convert = input("Which conversion do you want to use?: ").lower()
    if which_convert in conversion_dict:
        convert_it = conversion_dict[which_convert]
        num_converted = float(input("Enter your value of the base unit: "))
        print("The converted value is: " + str(convert_it(num_converted)))
    elif which_convert not in conversion_dict:
        print("Give a valid supported conversion.")
        convert_from_user()


convert_from_user()
