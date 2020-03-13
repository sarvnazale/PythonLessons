# comment (everything to the right of the pound symbol): good for reminders
# documentation (equivalent to readme)

# Words, characters, cannot be operated on, can on be concatenated
word = "7" # string datatype

# Numbers can be operated on (+, -, *, /, %) % is callled "modulo*"
number = 7          # INTEGER or int, whole number only
number_2 = 5.5      # float, only with decimals

switch = True       # boolean datatype, can only be True or False 

quotient = number / number_2 #Datatype ?? Float - dividing int by float results in a float
quotient2 = 4 / 2 #Datatype ?? Float - division always results in flaot 

# // gives integer division, i.e. the decimal is dropped
quotient3 = 5 // 2 #Datatype ?? Integer

# conversions
intConvert = int(4.9) # int() converts to integer, ALWAYS ROUNDS DOWN

#Concatenation - combining two strings together
stringA = "hello"
stringB = "world"

concatString = stringA + " " + stringB

print(concatString)
