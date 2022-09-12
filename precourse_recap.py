
def printMyString(aNumber, aString):
    print('My name is ' + aString + ',' + "and I am " + str(aNumber) + ' years old.')


myName = 'James'
myNumber = 32

printMyString(myNumber, myName)

def printMyDob(aNumber, aYear):
    print('I was born in the year ' + str(aYear - aNumber))

aYear = 2022

printMyDob(myNumber, aYear)