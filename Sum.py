''' 
This program calculates the sum of all number in a list
'''

def Addition(): 
    print("-------------------- Addition --------------------")
    print('Welcome to Addition!')
    input_string = input('To begin, enter a list of numbers separated by spaces.')
    sumlist = input_string.split()

    tokens = 12
    try:
        for i in range(len(sumlist)):
            sumlist[i] = float(sumlist[i])
            ans = 'default'

        Sum = 0
        if len(sumlist) > 1:
            for num in sumlist:
                Sum = Sum + num

        else:
            Sum = sumlist[0]
            print("There is only one number in this set. It is",Sum)
            tokens = 11

        if tokens != 11:
            print("The sum is", Sum)
    except ValueError:
        print("We're sorry, there are non-numeric characters in the list (Did you use words? We don't support words). Please try again.")
    
    print("\nWould you like to try again? (yes or no, all capitals)")
    yesNo = input()
    if yesNo == "YES":
        print("As you wish.")
        Addition()
    else:
        if yesNo == 'NO':
            print("As you wish")
            quit()
        else:
            print("Yes or no, all capitals")
            yesNo = input()
            if yesNo == "YES":
                print("As you wish.")
                Addition()
            else:
                if yesNo == 'NO':
                    print("As you wish")
                    quit()
                else:
                    print("*Sigh*")
                    print("END OF PROGRAM")
                    quit()

Addition()