def EVEN_OR_ODD():
    print("------------------------------ Even or Odd? ------------------------------------")
    print("""Welcome to Even or Odd! Type an integer to see if it is even or odd.""")
   
    response = input();
    try:
        num = int(response)
        REM = num%2 
   
        if REM == 0:
            print('EVEN!')
            exit()
        else:
            print("ODD!")
   
    except ValueError:
        print('''We're sorry, that's not an integer (Did you use words? We don't support words). 
Remember, even/odd classification doesn't apply to decimals. Please try again.''')       
    
    
    print("\nWould you like to try again? (yes or no, all capitals)")
    yesNo = input()
    if yesNo == "YES":
        print("As you wish.")
        EVEN_OR_ODD()
    else:
        if yesNo == 'NO':
            print("As you wish")
            quit()
        else:
            print("Yes or no, all capitals")
            yesNo = input()
            if yesNo == "YES":
                print("As you wish.")
                EVEN_OR_ODD()
            else:
                if yesNo == 'NO':
                    print("As you wish")
                    quit()
                else:
                    print("*Sigh*")
                    print("END OF PROGRAM")
                    quit()                     
EVEN_OR_ODD()