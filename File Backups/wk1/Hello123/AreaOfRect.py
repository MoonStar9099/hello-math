def AreaOfRect():
    
    print("------------------------ Area of Rectangle -------------------") 
    
    print('Welcome to Area of Rectangle (or square)!')
    
    print('What is the base of the rectangle? (Integer and float values only)') #For a good UI

    try: #to see if the values are not integers or floats
        base = float(input())
        print('What is the height of the rectangle?')
        height = float(input())
        area = base*height
        print("The area is,", area)
    except ValueError:
        print("We're sorry, that is not an integer. (Did you use words? We don't support words) Please try again.") 
    print("\nWould you like to try again? (yes or no, all capitals)")
    yesNo = input()
    if yesNo == "YES":
        print("As you wish.")
        AreaOfRect()
    else:
        if yesNo == 'NO':
            print("As you wish")
            quit()
        else:
            print("YES or NO, ALL CAPITALS")
            yesNo = input()
            if yesNo == "YES":
                print("As you wish.")
                AreaOfRect()
            else:
                if yesNo == 'NO':
                    print("As you wish")
                    quit()
                else:
                    print("*Sigh*")
                    print("END OF PROGRAM")
                    quit()

AreaOfRect()