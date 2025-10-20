import pandas

data= pandas.read_csv("weather_data.csv")
# print(type(data))
temp_data_list= data["temp"].to_list()

print(temp_data_list)
print(type(temp_data_list))

# data_dict= data.to_dict()
# print(data_dict)