
def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print(power(4, 4))
print(factorial(5))
