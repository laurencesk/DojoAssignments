l = ['magical unicorns',19,'hello',98.98,'world']

sum = 0
string =""
datatype = 0
intCount = 0
strCount = 0
listLen = len(l)

for i in range(0,len(l)):

    if type(l[i]) is int or type(l[i]) is float:
        sum+=l[i]
        intCount+=1

    elif type(l[i]) is str:
        string+=l[i]
        strCount+=1

if listLen == intCount:
    print "The list you entered is of integer type"
    print "Sum = ",sum

elif listLen == strCount:
    print "The list you entered is of integer type"
    print "String = ",string


elif listLen != strCount or listLen != intCount:
    print "The list you entered is of mixed type"
    print "Sum = ",sum
    print "String = ",string
