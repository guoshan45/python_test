# Write a program that maps a list of words into a list of integers
# representing the lengths of the correponding words.


listOfWords = ["words", "into", "integers"]
listOfInts = []

for i in range(len(listOfWords)):
    listOfInts.append(len(listOfWords[i]))

print("List of words:" + str(listOfWords))
print("List of wordlength:" + str(listOfInts))
