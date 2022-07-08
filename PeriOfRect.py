def PeriOfRect():
    
    print("------------------------ Perimeter of Rectangle -------------------") 
    
    print('Welcome to Perimeter of Rectangle (or square)!')
    
    print('What is the base of the rectangle? (Integer and float values only)')

    try: #to see if the values are not integers or floats
        base = float(input())
        print('What is the height of the rectangle?')
        height = float(input())
    except ValueError:
        print("We're sorry, that is not an integer. (Did you use words? We don't support words) Please try again.")
    peri = (base * 2) + (height * 2)
    print("The perimeter is", peri)
    print("\nWould you like to try again? (yes or no, all capitals)")
    yesNo = input()
    if yesNo == "YES":
        print("As you wish.")
        PeriOfRect()
    else:
        if yesNo == 'NO':
            print("As you wish")
            quit()
        else:
            print("Yes or no, all capitals")
            yesNo = input()
            if yesNo == "YES":
                print("As you wish.")
                PeriOfRect()
            else:
                if yesNo == 'NO':
                    print("As you wish")
                    quit()
                else:
                    print("*Sigh* End of program.")
                    quit()
PeriOfRect()