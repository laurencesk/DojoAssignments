# Find and Replace

words = "It's thanksgiving day. It's my birthday,too!"
positionOfDay = str.find(words,"day")
print positionOfDay
newWords = str.replace(words,"day","month")
print(newWords)


# Min and Max
x = []
listMax = max(x)
print(listMax)
listMin = min(x)
print(listMin)


# First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
first = x[0]
last = x[-1]
print first,last


# New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
xSort = sorted(x)
arrLen = len(x)
newArr1 = xSort[:arrLen/2]
newArr2 = []
newArr2.append(newArr1)
for i in range(0, arrLen/2+1):
    newArr2.append(xSort[arrLen/2:][i])
print newArr2
