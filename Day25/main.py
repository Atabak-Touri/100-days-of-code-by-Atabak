# # with open("weather_data.csv") as weather_data:
# #     data = weather_data.readlines()
# #     print(data)
#
# import csv
# with open("weather_data.csv") as weather_data:
#     data= csv.reader(weather_data)
#     temperature= []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
# How to create a dataframe from scratch
import pandas

data_dict = {
    "students": ["Andy", "Josi", "Maria"],
    "scores" : [16,56, 65]
}
data= pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)
