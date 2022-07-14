import fibonacci
import MaxNum
import MinNum
import PeriOfRect
import Sum
import Difference
import ReverseList
import EvenOrOdd
import PeriOfRect
import AreaOfRect

print("-------------------- Basic Math: A Simple Program --------------------")
print('Welcome to Basic Math!')
def Home():
    print('''\nSelect one of the following actions by typing it's number:\n------------------------------------------------------------------------
Area of Rectangle - 1\nPerimeter of Rectangle - 2\nList: Even or Odd? - 3\nAddition - 4''')
    print('''Subtraction - 5\nGreatest Number - 6\nLeast Number - 7\nEven or Odd - 8\nReverse List - 9\nFibonacci Sequence - 10\nquit - 11
------------------------------------------------------------------------''')
    userChoice = input()
    if userChoice == '1':
        print("As you wish.")
        AreaOfRect()
    elif userChoice == '2':
        print("As you wish.")
        PeriOfRect()
    elif userChoice == '3':
        print("As you wish.")
        ListOddEven()
    elif userChoice == '4':
        print("As you wish.")
        Addition()
    elif userChoice == '5':
        print("As you wish.")
        Subtraction()
    elif userChoice == '6':
        print("As you wish.")
        MaxNum()
    elif userChoice == '7':
        print("As you wish.")
        MinNum()
    elif userChoice == '8':
        print("As you wish.")
        EVEN_OR_ODD()
    elif userChoice == '9':
        print("As you wish.")
        ReverseList()
    elif userChoice == '10':
        FibonacciSequence()
    elif userChoice == '11':
        print("As you wish.")
        quit()
    else:
        print("That's not an option. Please try again.")
        Home()
'''
def AreaOfRect():
    
    print("------------------------ Area of Rectangle -------------------") 
    
    print('Welcome to Area of Rectangle (or square, parallelogram, or trapezoid)!')
    
    print('What is the base of the quadrilateral? (Integer and float values only)')

    try:
        base = float(input())
        print('What is the height of the quadrilateral?')
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
            Home()
        else:
            print("YES or NO, ALL CAPITALS")
            yesNo = input()
            if yesNo == "YES":
                print("As you wish.")
                AreaOfRect()
            else:
                if yesNo == 'NO':
                    print("As you wish")
                    Home()
                else:
                    print("*Sigh*")
                    print("END OF PROGRAM")
                    Home()
def PeriOfRect():
    
    print("------------------------ Perimeter of Rectangle -------------------") 
    
    print('Welcome to Perimeter of Rectangle (or square)!')
    
    print('What is the base of the quadrilateral? (Integer and float values only)')

    try: #to see if the values are not integers or floats
        base = float(input())
        print('What is the height of the rectangle?')
        height = float(input())
        
        peri = (base * 2) + (height * 2)
        print("The perimeter is", peri)
    
    except ValueError:
        print("We're sorry, that's not a number (Did you use words? We don't support words). Please try again.")
    
    
    print("\nWould you like to try again? (yes or no, all capitals)")
    yesNo = input()
    if yesNo == "YES":
        print("As you wish.")
        PeriOfRect()
    else:
        if yesNo == 'NO':
            print("As you wish")
            Home()
        else:
            print("Yes or no, all capitals")
            yesNo = input()
            if yesNo == "YES":
                print("As you wish.")
                PeriOfRect()
            else:
                if yesNo == 'NO':
                    print("As you wish")
                    Home()
                else:
                    print("*Sigh* End of program.")
                    Home()
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
            Home()
        else:
            print("Yes or no, all capitals")
            yesNo = input()
            if yesNo == "YES":
                print("As you wish.")
                ListOddEven()
            else:
                if yesNo == 'NO':
                    print("As you wish")
                    Home()
                else:
                    print("*Sigh*")
                    print("END OF PROGRAM")
                    Home()
def Addition(): 
    print("-------------------- Addition --------------------")
    print('Welcome to Addition!')
    input_string = input('To begin, enter a list of numbers separated by spaces.')
    sumlist = input_string.split()

    tokens = 12
    try:
        for i in range(len(sumlist)):
            sumlist[i] = float(sumlist[i])

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
            Home()
        else:
            print("Yes or no, all capitals")
            yesNo = input()
            if yesNo == "YES":
                print("As you wish.")
                Addition()
            else:
                if yesNo == 'NO':
                    print("As you wish")
                    Home()
                else:
                    print("*Sigh*")
                    print("END OF PROGRAM")
                    Home
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
            Home()
        else:
            print("Yes or no, all capitals")
            yesNo = input()
            if yesNo == "YES":
                print("As you wish.")
                MaxNum()
            else:
                if yesNo == 'NO':
                    print("As you wish")
                    Home()
                else:
                    print("*Sigh*")
                    print("END OF PROGRAM")
                    Home()
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
            Home()
        else:
            print("Yes or no, all capitals")
            yesNo = input()
            if yesNo == "YES":
                print("As you wish.")
                MinNum()
            else:
                if yesNo == 'NO':
                    print("As you wish")
                    Home()
                else:
                    print("*Sigh*")
                    print("END OF PROGRAM")
                    Home()
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
            Home()
        else:
            print("Yes or no, all capitals")
            yesNo = input()
            if yesNo == "YES":
                print("As you wish.")
                EVEN_OR_ODD()
            else:
                if yesNo == 'NO':
                    print("As you wish")
                    Home()
                else:
                    print("*Sigh*")
                    print("END OF PROGRAM")
                    Home()
'''
def ReverseList():
    print("-------------------- Reverse List --------------------")
    print('Welcome to Reverse List!')
    print('To begin, enter a list of characters separated by spaces.')
    input_string = input()
    lista = input_string.split()
    inputList = lista[0:(len(lista))]

    resultList = lista[0:(len(lista))]
    for val in lista[0:len(lista)]:
            resultList[((len(lista))-1):(len(lista))] = val
            lista = lista[:-1]
    print(resultList)
    lista = inputList[0:(len(inputList))]
    
    print("\nWould you like to try again? (yes or no, all capitals)")
    yesNo = input()
    if yesNo == "YES":
        print("As you wish.")
        ReverseList()
    else:
        if yesNo == 'NO':
            print("As you wish")
            Home()
        else:
            print("Yes or no, all capitals")
            yesNo = input()
            if yesNo == "YES":
                print("As you wish.")
                ReverseList()
            else:
                if yesNo == 'NO':
                    print("As you wish")
                    Home()
                else:
                    print("*Sigh*")
                    print("END OF PROGRAM")
                    Home()
def Subtraction(): 
    print("-------------------- Subtraction --------------------")
    print('Welcome to Subtraction!')
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
    input()
    yesNo = input()
    if yesNo == "YES":
        print("As you wish.")
        Subtraction()
    else:
        if yesNo == 'NO':
            print("As you wish")
            Home()
        else:
            print("Yes or no, all capitals")
            yesNo = input()
            if yesNo == "YES":
                print("As you wish.")
                Subtraction()
            else:
                if yesNo == 'NO':
                    print("As you wish")
                    Home()
                else:
                    print("*Sigh*")
                    print("END OF PROGRAM")
                    Home()
def fibonacci():
    FibonacciSequence()
'''    
Home()