def soltion():
    value = input('Enter list of numbers seperated with , after each number')

    nums = value.split(',')

    result = tuple(nums)

    print(result)


soltion()
