import pandas

data= pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Gray_sqrl= data[data["Primary Fur Color"] == "Gray"]
Cinnamon_sqrl= data[data["Primary Fur Color"] == "Cinnamon"]
Black_sqrl= data[data["Primary Fur Color"] == "Black"]

print(len(Gray_sqrl))
print(len(Cinnamon_sqrl))
print(len(Black_sqrl))

data_dict= {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [Gray_sqrl,Cinnamon_sqrl,Black_sqrl]
}
df=pandas.DataFrame(data_dict).to_csv("Squirrel Count")












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
# import pandas
#
# data_dict = {
#     "students": ["Andy", "Josi", "Maria"],
#     "scores" : [16,56, 65]
# }
# data= pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)
