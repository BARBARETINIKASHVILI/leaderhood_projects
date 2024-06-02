def dig_pow(n, p):
    
    number = 0
    for number in str(n):
        number +=  int(number) ** p
        p += 1

    return 1
