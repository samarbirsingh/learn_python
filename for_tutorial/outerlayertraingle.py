def outer_layer_triangle(parameter):
    for i in range(parameter):
        if i == 0:
            print(" " * (parameter - i - 1) + "*")
        elif i == parameter - 1:
            print("* " * parameter)
        else:
            print(" " * (parameter - i - 1) + "*", end="")
            print(" " * (2 * i - 1), end="")
            print("*")

parameter = 6
outer_layer_triangle(parameter)
