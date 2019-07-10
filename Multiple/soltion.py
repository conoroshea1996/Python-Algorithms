def soltion():
    x = int(input('Enter Number'))
    nums = dict()

    for i in range(1, x+1):
        nums[i] = i * i

    print(nums)


print(soltion())
