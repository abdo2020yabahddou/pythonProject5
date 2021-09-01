if __name__ == '__main__':
    num1=float(raw_input("please enter the first number:"))
    operator = raw_input("please enter the operator:")
    num2=float(raw_input("please enter the second number:"))
    if operator=="+":
        print (num1+num2)
    elif operator=="-":
        print (num1-num2)
    elif operator=="*":
        print (num1*num2)
    elif operator=="/":
        print (num1/num2)
    elif operator=="=":
        print (num2)
    else:
        print ("wrong operator try again")

