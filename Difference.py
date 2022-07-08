def Subtraction(): 
    print("-------------------- Addition --------------------")
    print('Welcome to Addition!')
    input_string = input('To begin, enter a list of numbers separated by spaces.')
    minusList = input_string.split()

    tokens = 12
    try:
        for i in range(len(minusList)):
            minusList[i] = float(minusList[i])
            Minus = 0
        if len(minusList) > 1:
            for num in minusList:
                Minus = Minus + num

        else:
            Minus = minusList[0]
            print("There is only one number in this set. It is", Minus)
            tokens = 11

        if tokens != 11:
            print("The difference is", Minus)
    except ValueError:
        print("Sorry, that's not an integer (Did you use words? We don't support words). Please try again.")
    print("\nWould you like to try again? (yes or no, all capitals)")
    yesNo = input()
    if yesNo == "YES":
        print("As you wish.")
        Subtraction()
    else:
        if yesNo == 'NO':
            print("As you wish")
            quit()
        else:
            print("Yes or no, all capitals")
            yesNo = input()
            if yesNo == "YES":
                print("As you wish.")
                Subtraction()
            else:
                if yesNo == 'NO':
                    print("As you wish")
                    quit()
                else:
                    print("*Sigh*")
                    print("END OF PROGRAM")
                    quit()

Subtraction()