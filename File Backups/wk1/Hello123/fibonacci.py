def FibonacciSequence():
    print('-------------------- Fibonacci Sequence Generator --------------------')
    print('Welcome to Fibonacci sequence generator!')
    print('Type any number to begin. This number will be the start of your custom sequence!')
    try:
        before = 0
        start = int(input())
        after = start
        print("How long do you want your sequence to be?")
        lenSeries = int(input())
        nextElement = before + after
        print(start)
           
        while lenSeries > 0:
            print(nextElement)
            placeHold1 = after
            placeHold2 = before
            before = placeHold1 + placeHold2
            after = nextElement
            nextElement = after + before
            lenSeries-=1
            
    except ValueError:
        print("Sorry, that's not an integer (Did you use words? We don't support words. Please try again.")
FibonacciSequence()()