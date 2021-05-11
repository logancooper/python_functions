#VARIABLES
phonebook_dict = {
  'alice': '703-493-1834',
  'bob': '857-384-1234',
  'elizabeth': '484-584-2923'
}

def lookUpNumber(phonebook):
    printDivider()
    print("Please enter the name of the entry you would like to look up: ")
    name = input()
    name = name.lower()
    if(name in phonebook):
        print(name + "'s phone number is: " + phonebook_dict[name])
    else:
        print(name + " is not in the phone book")

def createEntry(phonebook):
    printDivider()
    name = input("Please enter the name of the person you would like to create: ")
    name = name.lower()
    number = input("Please enter the phone number for " + name + ": ")
    phonebook_dict[name] = number
    print("An entry for " + name + " has been created in the phone book with the number: " + phonebook_dict[name])

def deleteEntry(phonebook):
    printDivider()
    name = input("Please enter the name of the person you would like to delete: ")
    name = name.lower()
    del phonebook[name]
    print(name + " has been deleted from the phone book")

def listAllEntries(phonebook):
    printDivider()
    for key, value in phonebook.items():
        print("%s's phone number is %s" % (key, value))

def quit():
    exit()

def functionChoice():
    printDivider()
    myInput = input("Please choose a function: \nEnter 1 to lookup by name\nEnter 2 to create a new entry\nEnter 3 to delete an entry by name\nEnter 4 to print all entries\nEnter 5 to quit\n")
    
    if myInput:
        myInput = int(myInput)
        if(myInput == 1):
            lookUpNumber(phonebook_dict)
            functionChoice()
        elif(myInput == 2):
            createEntry(phonebook_dict)
            functionChoice()
        elif(myInput == 3):
            deleteEntry(phonebook_dict)
            functionChoice()
        elif(myInput == 4):
            listAllEntries(phonebook_dict)
            functionChoice()
        elif(myInput == 5):
            quit()
        else:
            print("Your input was invalid!")
            functionChoice()

def printDivider():
    print("-----------------------------------------------")
# phonenumber(phonebook_dict)
# add_to_dict(phonebook_dict)
# delete_alice(phonebook_dict)
# change_bob_number(phonebook_dict)
# print_all_phone_numbers(phonebook_dict)


#USER INPUT
print("Welcome to the phone book app. ")
functionChoice()