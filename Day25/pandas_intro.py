import pandas

data= pandas.read_csv("weather_data.csv")
# print(type(data))
# temp_data_list= data["temp"].to_list()
# avg_temp= sum(temp_data_list)/ len(temp_data_list)
# print(data["Condition"])
# print(data.Condition)
# print(type(temp_data_list))
# print(data["temp"].max())
# data_dict= data.to_dict()
# print(data_dict)
# print(data[data.temp == data["temp"].max()])
monday = data[data.day == "Monday"]
monday_F=monday["temp"] * 9/5 + 32
print(monday_F)