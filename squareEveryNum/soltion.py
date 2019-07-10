def soltion():
    list = input('Enter Numbers List \n >')
    nums = [x for x in list.split(',') if int(x) % 2 == 0]
    print(nums)


soltion()
