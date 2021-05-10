userInputName = ""
userInputTitle = ""
userInfo = []
def greeting(name, title):
    return("This is %s, the %s " % (name,title))
def userInput():
    userInputName = input("What is your name?")
    userInputTitle = input("What is your title?")
    return [userInputName, userInputTitle]
def userInput_Dict():
    userInputName = input("What is your name?")
    userInputTitle = input("What is your title?")
    return {"name" : userInputName,
            "title": userInputTitle
    }

userInfo = userInput_Dict()
greetingString = greeting(userInfo["name"], userInfo["title"])
print(greetingString)