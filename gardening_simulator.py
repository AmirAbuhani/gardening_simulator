snow_mount = 20
dictionary = {"folwering_plants": {"weather": "sun", "precipitation number": 40, "is_wind": "wind"},
              "conifers": {"weather": "clouds", "precipitation number": 70, "is_wind": "no"},
              "ferns": {"weather": "sun", "precipitation number": 20, "is_wind": "wind"}}

weather_today = input("sun or clouds: ")
for item in dictionary:
    if weather_today == dictionary[item]["weather"]:
        print(item)
precipitation_number = int(input("Enter how much water do they need "))
for item in dictionary:
    if precipitation_number == dictionary[item]["precipitation number"]:
        print(item)
wind_or_not = input("wind or no: ")
for item in dictionary:
    if wind_or_not == dictionary[item]["is_wind"]:
        print(item)

for item in dictionary:
    dictionary[item].update({"snow_mount": +snow_mount})
    snow_mount += 20

print(dictionary)

snow_info = int(input("amount of snow:  "))
for item in dictionary:
    if dictionary[item]["snow_mount"] > snow_info:
        print(f"{item} will dead")
