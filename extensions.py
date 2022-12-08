def all_one_bin(size):
    return int(bin((2**size)-1), 2)

def list_to_bin(list):
    b = 0
    for val in list:
        b = 2 * b + val
    return b