def expo(b,p):
    base = float(b)
    power= int(p)
    result = 1

    for i in range(power):
        result = result * base
    return result

e = expo(input("Enter a base value to be exponentiated:"),input("Enter a power as an integer"))
print(e)
