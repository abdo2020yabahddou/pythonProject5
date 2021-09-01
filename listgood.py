if __name__ == '__main__':
    name = ["cose","code","ahmed"]
    alpha = [123,"amin","allo"]
    My_name = list(name)
    My_name_copy = name[:]
    print (My_name)
    alpha.sort()
    print (alpha)
    name.append("afraid")
    name.insert(0,"aswat")
    name.remove("code")
    name.pop()
    print (name)
    poped = name.pop()
    print (poped)
    print (alpha.index("allo"))
    print (alpha.count("allo"))
    print (name + alpha)
    name.extend(alpha)
    print (name)
    name += alpha
    print (name)
