## ask user to open file, then store it in 'textFile'
textFile = input("Enter the file name: ")
try:
    textFile = open(textFile)
except:
    print('File cannot be opened:', textFile)
    exit()

## creates blank dictionary object
storedWords = dict()

## outer loop parses textFile by line
for line in textFile:
    ## splits the line by the space delimeter and creates a list
    words = line.split()
    ## parses the list and adds 1 to the dictionary key
    for word in words:
        if word not in storedWords:
            storedWords[word] = 1
        else:
            storedWords[word] += 1

print("Search for specific words in the file, using the following command:")
print(" 'word' in storedWords")


    
