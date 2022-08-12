'''
Created on Jan. 5, 2022

@author: INR
'''
#lista = [3, 7, 23, 17, 9]
#lista = [2, 5, 7, 9, 10, 15]
lista = [2, 4, 6, 8, 10, 16]
#lista = [1]
#lista = [2]
#lista = ['hehe']
ans = "default"
temp = lista[0]

if type(lista[0]) == str:
    ans = "There are non-numeric characters in this list. Please try again."
    print(ans)
    quit()
if (temp%2 == 0 and len(lista) > 1):
    #print("length =", len(lista))
    for val in lista[1:(len(lista))]:
        REM = val % 2
        #print('val =', val)
        if REM != 0:
            ans = "This list is neither even or odd."
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

if type(lista[0]) == str:
    ans = "There are non-numerical characters in this list. Please try again."

print(ans)
