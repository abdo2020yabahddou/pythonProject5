if __name__ == '__main__':
    convert_animals={"1":"Lion","Lio":0,"ele":"elefant,it doesn't main"}
    print (convert_animals["ele"])
    print (convert_animals["1"])
    print (convert_animals.get("Lio","it does exist"))