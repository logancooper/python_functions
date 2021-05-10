#VARIABLES
num_list = []
numberCapture = 0
string_list = []
stringCapture = ""
def captureNumbers():
    numberCapture = input("Please enter a number: ")
    if numberCapture:
        num_list.append(int(numberCapture))
        captureNumbers()
    else:
        print("Your number list is: ")
        print(num_list)
def captureStrings():
    stringCapture = input("Please enter a string: ")
    if stringCapture:
        string_list.append(stringCapture)
        captureStrings()
    else:
        print("Your string list is: ")
        print(string_list)
#Largest number
def largestInList(mylist):
    printDivider()
    largest = mylist[0]
    for number in mylist:
        if(number > largest):
            largest = number
    print("The largest number of your list is: " + str(largest))
#Smallest Number
def smallestInList(mylist):
    printDivider()
    smallest = mylist[0]
    for number in mylist:
        if(number < smallest):
            smallest = number
    print("The smallest number of your list is: " + str(smallest))
#Shortest string in list of strings
def shortestString(myStringList):
    smallestText = myStringList[0]
    for string in myStringList:
        if (len(string) < len(smallestText)):
            smallestText = string
    print("The smallest string in your list is: " + smallestText)
    return smallestText
#Longest string in list of strings
def longestString(myStringList):
    longestText = myStringList[0]
    for string in myStringList:
        if (len(string) > len(longestText)):
            longestText = string
    print("The longest string in your list is: " + longestText)
    return longestText
def functionChoice():
    printDivider()
    myInput = input("Please choose a function: \nEnter 1 to find the lowest number in the number list\nEnter 2 to find the largest number in the number list\nEnter 3 to find the smallest string in the string list\nEnter 4 to find the longest string in the string list\n")
    
    if myInput:
        myInput = int(myInput)
        if(myInput == 1):
            smallestInList(num_list)
            functionChoice()
        elif(myInput == 2):
            largestInList(num_list)
            functionChoice()
        elif(myInput == 3):
            shortestString(string_list)
            functionChoice()
        elif(myInput == 4):
            longestString(string_list)
            functionChoice()
        else:
            print("Your input was invalid!")
            functionChoice()

def printDivider():
    print("-----------------------------------------------")
    
#USER INPUT
print("Enter a series of numbers to add to the number list. When you are finished, press enter to continue.")
captureNumbers()
print("Enter a series of strings to add to the string list. When you are finished, press enter to continue.")
captureStrings()
functionChoice()