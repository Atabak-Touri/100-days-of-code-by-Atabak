import re
def format_name(f_name, l_name):  #get this variables as input
    if f_name== "" or l_name=="":
        return "The input is not valid"
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()
    return f"My first name is {formated_f_name}, and my last name is {formated_l_name}."
    # print(f"My first name is {formated_f_name}, and my last name is {formated_l_name}.")

formated_string= format_name(input("what is your first name?"), input("What is your last name?"))
print(formated_string)


