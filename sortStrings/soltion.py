def soltion():
    words = [x for x in input(
        'Enter your lsit of words seperated with , after each \n >').split(',')]
    print(words)
    words.sort()
    print(words)


soltion()
