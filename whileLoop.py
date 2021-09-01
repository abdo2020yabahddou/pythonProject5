if __name__ == '__main__':
    I =1
    while I<=3 :
        print (I)
        I +=2
    while I<=2:
        print (I)
        I +=1
    else:
        print ("fine")
    print ("has ended")
    O=2
    while O<=8:
        print (O)
        O+=1
    else:
        print ("good")
    J=2
    while J <=8:
        J +=1
        if J==4:
            continue
        elif J==7:
            break
        print (J)