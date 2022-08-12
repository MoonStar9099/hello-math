'''
Created on Jan. 12, 2022

@author: THINKPADINR
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
            quit()
        else:
            print("Yes or no, all capitals")
            yesNo = input()
            if yesNo == "YES":
                print("As you wish.")
                ReverseList()
            else:
                if yesNo == 'NO':
                    print("As you wish")
                    quit()
                else:
                    print("*Sigh*")
                    print("END OF PROGRAM")
                    quit()
ReverseList()
