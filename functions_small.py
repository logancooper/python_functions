inputList = [1,4,2,25,43,44]

def celciusToFahrenheit(celcius):
    return ((celcius*(9/5)) + 32)

def FahrenheitToCelcius(fahrenheit):
    return ((fahrenheit - 32) * (5/9))

def is_even(number):
    if(number % 2 == 0):
        return True
    else: return False

def is_odd(number):
    if(number % 2 != 0):
        return True
    else: return False

def only_evens(inputList):
    returnList = []
    for number in inputList:
        if(number % 2 == 0):
            returnList.append(number)
    return returnList

def only_odds(inputList):
    returnList = []
    for number in inputList:
        if(number % 2 != 0):
            returnList.append(number)
    return returnList
    


print(celciusToFahrenheit(20))
print(FahrenheitToCelcius(68))
print(is_even(2))
print(is_odd(2))
print(only_evens(inputList))
print(only_odds(inputList))