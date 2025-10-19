# file = open("my_file.txt")
# contents = file.read() #as a string
# print(contents)
#
# file.close() #once  python opens the file, it uses some resources. so we need to close it!

# with open("my_file.txt") as file: #by defult it is read only!
#     contents = file.read()  # as a string
#     print(contents)

with open("my_file.txt", mode= "w") as file: #change the mode to write only. this will replace the whole text file with the new input
    file.write("Hi")

with open("my_file.txt", mode="a") as file:
    file.write("this is example for appending")

with open("new_file.txt", mode="w") as file: #only works in write mode and when the file does not exist
    file.write("\n Hey this file is made up from scratch by Python")

