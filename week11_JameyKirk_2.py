import string

textFile = input("Enter the file name: ")
try:
    textFile = open(textFile)
except:
    print('File cannot be opened:', textFile)
    exit()

## creates blank dictionary object
storedWords = dict()

for line in textFile:
    ## splits the line by the space delimeter and creates a list
    words = line.split()
    ## parses the list and adds 1 to the dictionary key
    for word in words:
        if word not in storedWords:
            storedWords[word] = 1
        else:
            if word.find('@') > 0:
                storedWords[word] += 1
            else:
                storedWords[word] = 1

for textStr in storedWords:
    if storedWords[textStr] > 1:
        print(textStr, storedWords[textStr])
