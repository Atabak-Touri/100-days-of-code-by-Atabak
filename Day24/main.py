file = open("my_file.txt")
contents = file.read() #as a string
print(contents)

file.close() #once  python opens the file, it uses some resources. so we need to close it!