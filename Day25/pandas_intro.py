import pandas

data= pandas.read_csv("weather_data.csv")
# print(type(data))
temp_data_list= data["temp"].to_list()
avg_temp= sum(temp_data_list)/ len(temp_data_list)
"""summary statistics"""

print(data["temp"].max())
print(data["temp"].mean())
print(avg_temp)
# print(type(temp_data_list))

# data_dict= data.to_dict()
# print(data_dict)