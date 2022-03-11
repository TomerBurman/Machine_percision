def machine_precision():
    '''
    finds the machine precision in current environment (32bit/64bit)
    :return: none
    '''
    x, temp, eps = 1, 0, 0.0
    while (x + 1 != 1):
        eps = x
        x /= 2
        temp += 1
    print(f"Smallest number: {eps}, iterations: {temp}")

