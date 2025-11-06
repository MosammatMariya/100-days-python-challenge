
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def pow(a,b):
    return a**b

operation = {"+" : add, "-" : sub, "*" : mul, "/" : div, "^" : pow}

def calculate() :
    print(logo.art)
    print("**** Welcome to Calculator ****")
  
    to_be_continued = True
  
    c = float(input("what is your first number? "))
  
    print("what operator you will use?\n+\n-\n* \n/ \n^")

    while to_be_continued:
        operator = input("Your operation:")

        d = float(input("what is your second number? "))

        answer = operation[operator](c, d)

        print(f"{c} {operator} {d} = {answer}")

        continue_math = input(f"Do you want to continue with {answer}? Type 'y' for yes or 'n' for no.\n").lower()
        if continue_math == "y":
            c = answer
        else:
            to_be_continued = False
            print("\n"* 20)
            calculate()

calculate()
