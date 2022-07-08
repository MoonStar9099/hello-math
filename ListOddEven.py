def ListOddEven():
    print("-------------------- List: Even or Odd? --------------------")
    print('Welcome to List: Even or Odd!')
    REM = 14
    input_string = input('To begin, enter a list of numbers separated by spaces.')
    lista = input_string.split()


    try:
        for i in range(len(lista)):
            lista[i] = float(lista[i])
            ans = "default"
            temp = lista[0]
    except ValueError:
        ans = "There are non-numerical characters in this list. Please try again."
        print(ans)
        quit()

    if type(lista) != str:
        if (temp%2 == 0 and len(lista) > 1):
            #print("length =", len(lista))
            while REM <= 0:    
                for val in lista[1:(len(lista))]:
                    REM = val % 2
                    #print('val =', val)
    else:
        ans = "There are non-numeric characters in this list. (Did you use words? We don't support words) Please try again."        

    if REM != 0:
        ans = "This list is neither even or odd.(Remember, only integers can be even or odd. That classification doesn't apply to decimals!)"
    else:
        ans = 'This list is even.'


    if (temp%2 != 0 and len(lista) > 1):
        for val in lista:
            REM = val%2
            #print(REM)
            #print(val)                
            if REM == 0:
                ans = "This list is neither even or odd."
                break
        
            else:
                ans = 'This list is odd.'
       


    if (len(lista) == 1 and temp%2 == 0):
        ans = "There is only one number in this list. It is even." 

    if (len(lista) == 1 and temp%2 != 0):
        ans = "There is only one number in this list. It is odd." 

    print(ans)
    print("\nWould you like to try again? (yes or no, all capitals)")
    yesNo = input()
    if yesNo == "YES":
        print("As you wish.")
        ListOddEven()
    else:
        if yesNo == 'NO':
            print("As you wish")
            quit()
        else:
            print("Yes or no, all capitals")
            yesNo = input()
            if yesNo == "YES":
                print("As you wish.")
                ListOddEven()
            else:
                if yesNo == 'NO':
                    print("As you wish")
                    quit()
                else:
                    print("*Sigh*")
                    print("END OF PROGRAM")
                    quit()

ListOddEven()