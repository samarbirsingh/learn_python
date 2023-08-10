def triangle(parameter):
    for i in range(1,parameter+1):
        print(" "* (parameter-i), end="") #print spaces
        print("*" * (2 * i - 1)) #print stars

parameter=6
triangle(parameter)
