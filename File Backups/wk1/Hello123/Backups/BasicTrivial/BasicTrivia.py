import random


def BasicTrivia():
    questionBank =  {'Bananas emit non-lethal levels of gamma radiation': True, 'Avacadoes emit more radiation than bananas': False,
                    "The tallest mountain in the solar system is on Jupiter": False, 'Grapes can kill a dog': True,
                    "Dogs can eat mangoes and bananas as special treats": True, "Blueberries can be used to teach dogs to catch treats in the air": True,
                    "'A' is the letter used most in the English language": False, 'In Harry Potter, Draco Malfoy has no siblings': False,
                    "The star sign Aquarius is represented by a tiger": True

                }


    usedBank = questionBank.copy()
    usedKeys = list(usedBank)
    currNum = 1
    totalQues = 5
    correctQues = 0
                
    def randomQues():
        return random.choice(usedKeys)

    #print(randomQues())
    
    def quesLogic():
        currQues = randomQues()
        currKey = str(currQues)
        currAns = usedBank[currKey]
        currNum = 1
        correctQues = 0
        usedBank.pop(currQues)
        usedKeys.remove(currKey)
                
        print("Q.",currNum, currQues, "\n True            False")
                
                
        try:
                    userInput = bool(input())
                    if userInput == currAns:
                        correctQues = correctQues + 1
                        currNum = currNum + 1
                    
        except ValueError:
                    print('question skipped')
                    totalQues = totalQues + 1
                    currNum = currNum + 1
        
        print("Your score:", (correctQues/totalQues)*100,'%')
            
        quesLogic()

BasicTrivia()
        
        