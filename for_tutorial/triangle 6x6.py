def triangle(parameter):
    for i in range(parameter):
        print(" " * (parameter - i - 1), end="")  # print spaces
        print("* " * (i + 1))  # print stars

parameter = 6
triangle(parameter)
