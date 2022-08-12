def MaxNum():
    print('-------------------- Greatest Number -------------------')
    print('Welcome to Greatest Number!')
    input_string = input('To begin, enter a list of numbers separated by spaces.')
    lista = input_string.split()

    try:
        for i in range(len(lista)):
            lista[i] = float(lista[i])            
        length = len(lista)
        max_num = lista[0]

        if length > 1:
            for num in lista:
                if  num > max_num:
                    max_num = num
        else:
            print("There is only one number in this set. It is", max_num)
            quit()

        print("The greatest number is", max_num)
    except ValueError:
        print("There are non-numerical characters in this list (Did you use words? We don't support words) Please try again.")
    
    print("\nWould you like to try again? (yes or no, all capitals)")
    yesNo = input()
    if yesNo == "YES":
        print("As you wish.")
        MaxNum()
    else:
        if yesNo == 'NO':
            print("As you wish")
            quit()
        else:
            print("Yes or no, all capitals")
            yesNo = input()
            if yesNo == "YES":
                print("As you wish.")
                MaxNum()
            else:
                if yesNo == 'NO':
                    print("As you wish")
                    quit()
                else:
                    print("*Sigh*")
                    print("END OF PROGRAM")
                    quit()
MaxNum()