
# this function takes in any number of arguments:
def arb_args(*args):
    for argument in args:
        print(argument)

#arb_args(27, "Quiche", ["dancing", "swimming", "walking"])


# nested functions performing math operations:
def inner_func(first_number, last_number):
    def first_inner_function(inner_func_arg):
        return first_number + last_number + inner_func_arg 
    def last_inner_function(inner_func_arg):
        return last_number - first_number + inner_func_arg 
    print(first_inner_function(88) + last_inner_function(11))

#inner_func(2727, 18)


# this function prints out strings and has a default argument
def lunch_lady(student_name, student_lunch="Mystery Meat"):
    print(f"Student: {student_name}\nLunch: {student_lunch}")

#lunch_lady("Bart")
#lunch_lady("Lisa", "Kale") 
#lunch_lady("Maggie", "Yogurt")


# this function return the sum and the product of two integers
def sum_and_product(first_int, last_int):
    return first_int + last_int, first_int * last_int

#print(sum_and_product(22, 20))


# this variable's value is assigned the arb_args function defined earlier in this file
alias_arb_args = arb_args

#alias_arb_args(5, 10, 15, "crackers")


# this function prints the average of integers passed in
def arb_mean(*integers_for_average):
    total = 0
    for _int in integers_for_average:
        total += _int
    print(total / len(integers_for_average))

#arb_mean(97, 100, 57, 99, 48, 86, 41, 54)


# this function finds the longest string passed in it
def arb_longest_string(*strings):
    current_longest_length = 0
    current_longest_string = ""
    for string in strings:
        if len(string) > current_longest_length:
            current_longest_length = len(string)
            current_longest_string = string
    return current_longest_string

longest = arb_longest_string("This", "is", "not", "the", "longest", "supercalifragilisticexpialidocious")

#print(longest)


