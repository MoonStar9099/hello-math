def Fibonacci():
    print('-------------------- Fibonacci Sequence --------------------')
    print('Welcome to Fibonacci sequence!')
    print('Type any number to begin. This number will be the start of your custom sequence!')
    try:
        before = 0
        start = int(input())
        print("How long do you want your sequence to be?")
        lenSeries = int(input())
        nextElement = before + start
        print(start)
           
        while lenSeries > 0:
            print(nextElement)
            placeHold1 = start
            placeHold2 = before
            start = placeHold1 + placeHold2
            before = nextElement
            nextElement = start + before
            lenSeries-=1
            
    except ValueError:
        print("Sorry, that's not an integer (Did you use words? We don't support words. Please try again.")
Fibonacci()