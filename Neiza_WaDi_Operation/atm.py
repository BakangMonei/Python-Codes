print('Welcome to Bank Of The Professor')
restart = ('Y')
chances = 3
balance = 999.12
while chances >= 0:
    pin = input(str('Please enter your 4 digit pin: '))
    if pin == (1234):
        print('Correct Pin!!')
        print('Please Press 1 for your Balance')
        print('Please Press 2 for Withdrawal')
        print('Please Press 3 to Deposit')
        print('Please Press 4 to Return Card\n')
        while restart not in ('n', 'NO', 'no', 'N'):
            print('Please Press 1 for your Balance')
            print('Please Press 2 for Withdrawal')
            print('Please Press 3 to Pay In')
            print('Please Press 4 to Return Card\n')
            option = int(input('What would you like to choose?: '))
            if option == 1:
                print('Your balance is: P', balance)
                restart = input('Would you like to go back? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank you!!')
                    break
                elif option == 2:
                    option = ('y', 'YES', 'yes', 'Yes')
                    withdrawal = float(input('How much would you like to withdraw? 10, 20, 40, 60, 80, 100 for other enter 1: '))
                    if withdrawal in [10, 20, 40, 60, 80, 100]:
                        balance = balance - withdrawal
                        print('\nYour new balance is now P', balance)
                        restart = input('Would you like to go back? ')
                        if restart in ('n', 'NO', 'no', 'N'):
                            print('Thank you!!')
                            break
                    elif withdrawal != [10, 20, 40, 60, 80, 100]:
                        print('\nInvalid amount, Please re-try')
                        restart = ('y', 'YES', 'yes', 'Yes')
                    elif withdrawal == 1:
                        withdrawal = float(input('Please enter your amount: '))
                elif option == 3:
                    Deposit = float(input('How much would you like to deposit? '))
                    balance = balance + deposit
                    print('\nYour new balance is now P', balance)
                    restart = input('Would you like to go back? ')
                    if restart in ('n', 'NO', 'no', 'N'):
                        print('Thank you!!')
                        break
                elif option == 4:
                    print('\nPlease wait for your card!!')
                    print('\nThank you for your services!!!')
                    break
                else:
                    print('Please enter the correct pin')
                    restart = ('y', 'YES', 'yes', 'Yes')
    elif pin != ('1234'):
        print('Incorrect pin')
        chances = chances - 1
        if chances == 0:
            print('\nPin blocked')
            break