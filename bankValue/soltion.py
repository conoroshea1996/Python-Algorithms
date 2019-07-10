def soltion():
    Bank = 0

    user_input = input(
        'Enter D + " " + amount to deposite or W + " " + amount to withdraw \n >')
    type_input = user_input.split(' ')[0]
    print(type_input)
    user_amount = user_input.split(' ')[1]
    user_amount_num = int(user_amount)
    print(user_amount_num)

    if type_input == 'D':
        Bank += user_amount_num
    elif type_input == 'W':
        Bank -= user_amount_num
    else:
        print('Error')

    print(Bank)


soltion()
