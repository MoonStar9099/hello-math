def MinNum():
    print("-------------------- Least Number --------------------")
    print('Welcome to Least Number!')
    input_string = input('To begin, enter a list of numbers separated by spaces.')
    lista = input_string.split()
    min_num = 12
    try:
        for i in range(len(lista)):
            lista[i] = float(lista[i])

    
        if len(lista) > 1:
            for num in lista:
                if  num < min_num:
                    min_num = num
        else:
            print("There is only one number in this set. It is", min_num)
            quit()
    
        print("The smallest number is", min_num)
    except ValueError:
        print("We're sorry, there are non-numerical characters in this list (Did you use words? We don't support words) Please try again.")
    
    print("\nWould you like to try again? (yes or no, all capitals)")
    yesNo = input()
    if yesNo == "YES":
        print("As you wish.")
        MinNum()()
    else:
        if yesNo == 'NO':
            print("As you wish")
            quit()
        else:
            print("Yes or no, all capitals")
            yesNo = input()
            if yesNo == "YES":
                print("As you wish.")
                MinNum()()
            else:
                if yesNo == 'NO':
                    print("As you wish")
                    quit()
                else:
                    print("*Sigh*")
                    print("END OF PROGRAM")
                    quit()
MinNum()