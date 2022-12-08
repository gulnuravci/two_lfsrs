def list_to_bin(list):
    b = 0
    for val in list:
        b = 2 * b + val
    return b