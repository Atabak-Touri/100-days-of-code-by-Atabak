# print("Hello World")
# num_char=len("Hello World")
# print(num_char)

def my_function():
    print("Hello")
    print("Bye")

my_function()


def my_function2(sky=None):
    if sky == "clear":
        print("It's a clear sky")
    elif sky == "cloudy":
        print("It's cloudy")
    else:
        print("It's not clear or cloudy")

