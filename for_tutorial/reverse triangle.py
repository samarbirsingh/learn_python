def reverse_equilateral_triangle(parameter):
    for i in range(parameter, 0, -1):
        print(" " * (parameter - i) + "* " * i)

parameter = 6
reverse_equilateral_triangle(parameter)
