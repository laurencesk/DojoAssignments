word_list = ['hello','world','my','name','is','Anna']
char = 'o'
newList = []

for i in range(0,len(word_list)):
    if char in word_list[i]:
        newList.append(word_list[i])
print newList
