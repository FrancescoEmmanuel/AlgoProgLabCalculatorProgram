
def add(num1,num2):
    return(num1 + num2)


def subs(num1,num2):
    return(num1 - num2)

def multi(num1,num2):
    return(num1 * num2)

def div(num1,num2):
    return(num1/num2)

def powr(num1,num2):
    return(num1**num2)

print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
print("5.power")

while True:
    op = input("select the operation you want to use: ")
    num1 = eval(input("enter the first number:"))
    num2 = eval(input("enter the second number: "))


    if op == "addition":
        print(num1, "+", num2, "=",round(add(num1, num2),1))
    elif op == "substraction":
        print(num1, "-", num2, "=",round(subs(num1, num2),1))
    elif op == "multiplication":
        print(num1, "x", num2, "=",round(multi(num1, num2),1))
    elif op == "division":
        print(num1, "/", num2, "=",round(div(num1, num2),1))
    elif op =="power":
        print(num1, "^", num2, "=",round(powr(num1, num2),1))
    else:
        print("you did not enter a valid operator!")
    
    stay = input("do u still wanna use the calculator(y/n)?")

    if stay == "n":
        print("damn see you next time then")
        break





