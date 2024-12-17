def pyramid(height):
    for i in range(1, height + 1):
        spaces = height - i
        stars = 2 * i - 1
        print(' ' * spaces + '*' * stars)
pyramid(5)
