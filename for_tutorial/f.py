def draw_pyramid(size):
    for i in range(1, size + 1):
        # Print spaces
        print(" " * (size - i), end="")
        # Print asterisks
        print("*" * (2 * i - 1))

# Set the size of the pyramid
pyramid_size = 6
draw_pyramid(pyramid_size)