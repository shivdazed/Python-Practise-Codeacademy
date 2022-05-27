def max(a,b,c):
    x=int(a)
    y=int(b)
    z=int(c)
    if x > y and x > z:
        return "1st number is largest"
    elif y > x and y > z:
        return "2nd number is largest"
    elif z > x and z > y:
        return "3rd number is largest"
    else:
        return "All are Equal"


m = max(11,12,13)
print(m)