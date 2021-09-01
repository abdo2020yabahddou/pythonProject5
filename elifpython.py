if __name__ == '__main__':
    def max_num(num1,num2,num3):
        if num1>=num2 and num1>=num3:
            return num1
        elif num2>=num1 and num2>=num3:
            return num2
        else:
            return num3
    value=max_num("12","15","30")
    print (value)
    def fox_rule(rule1,rule2):
        if rule1==rule2:
            print ("I am too")
        elif rule1==rule2:
            print ("go fight")
        else:
            print ("amin")
    rules=fox_rule("abllatif","abdelatif")

