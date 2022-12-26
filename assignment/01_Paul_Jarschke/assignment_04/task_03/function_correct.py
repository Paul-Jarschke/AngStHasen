def decimal_to_binary_correct(n):
    return int(bin(n).replace("0b", ""))


print(decimal_to_binary_correct(8))
