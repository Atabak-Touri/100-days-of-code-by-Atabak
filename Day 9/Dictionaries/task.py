programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
new=input("add a word to dic")
definition=input("what does it mean?")
for key in programming_dictionary:
    programming_dictionary[new]=definition
# print(programming_dictionary["Bug"])

# programming_dictionary["Loop"] = "The action of doing something over and over again."
#
# # print(programming_dictionary)
#
# # empty_dictionary={}
#
# # wipe an exicting dictionary
# for thing in programming_dictionary:
#     # print(key)
#     print(programming_dictionary[thing])
# print("Hello World!")
print(programming_dictionary)