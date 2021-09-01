if __name__ == '__main__':
    is_healthy=True
    if is_healthy:
        print ("go to the doctor")
        print ("you are so cute")
    else:
        print ("you are good")
    is_thirsty=False
    if is_thirsty==True:
        print ("Go drink")
    is_good=False
    is_not_good=True
    if is_good or is_not_good:
        print ("ta nod")
    is_good = False
    is_not_good = True
    if is_good and is_not_good==False:
        print ("ta nod")
    elif is_good and not is_not_good:
        print ("go swim")
    elif not is_good and is_not_good:
        print ("hallo")