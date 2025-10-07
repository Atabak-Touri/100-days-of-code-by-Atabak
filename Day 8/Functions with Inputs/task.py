# # def greet(input):
# #     print(f"Hello, {input}")
# #     print("This is Atabak")
# #     print("Nice to meet you!")
# #
# # greet("Reza")
# #
# # name = input("Enter your name: ")
# # location= input ("Where are you from:")
# # def greet (name, location):
# #     print(f"Hello, {name}")
# #     print("This is Atabak")
# #     print(f"Nice to hear that you're from {location}!")
# # greet(location= "nowhere", name="john")
# def calculate_love(name1, name2):
#     combined_name= (name1 + name2).lower()
#
#     true=0
#     for letters in "true":
#         if letters in combined_name:
#             true+=1
#     love = 0
#     for letters in "love":
#         if letters in combined_name:
#             love+=1
#     this = str(love) + str(true)
#     print(f"{name1} and {name2} love each other {this} times")
# calculate_love("reza", "atabak")

name= input("what is your name?")
location= input("where are you from?")
def greet_with(name=name, location=location):
    print(f"hello {name}")
    print(f"how is it in {location}?")
greet_with(name, location)