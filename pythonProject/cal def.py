def multi_result (a, b):
    return a * b
def add_result (a, b):
    return a + b

def sub_result(a,b):
    return a - b
def division_result(a,b):
    return a / b
def expon_results(a,b):
    return a ** b
def divisions_results(a,b):
    return a // b

a = int(input("please input your number:"))
b = int(input("what is the seond number:"))
operator = input("input operator:")

if operator == "+":
    print(add_result(a, b))
elif operator == "*":
    print(multi_result(a, b))

elif operator == "-":
    print(sub_result(a,b))
elif operator == "/":
    print(division_result(a,b))

elif operator == "**":
    print(expon_results(a, b))
elif operator == "//":
    print(divisions_results(a,b))


