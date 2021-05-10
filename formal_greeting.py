userInputName = ""
userInputTitle = ""

def greeting(name, title):
    return("This is %s, the %s " % (name,title))
def userInput():
    userInputName = input("What is your name?")
    userInputTitle = input("What is your title?")
    print(greeting(userInputName,userInputTitle))




