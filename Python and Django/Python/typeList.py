l = ['magical unicorns',19,'hello',98.98,'world']

sum = 0
string =""
datatype = 0

for i in range(0,len(l)):
    print i
    if type(l[i]) is int or type(l[i]) is float:
        sum+=l[i]

    elif type(l[i]) is str:
        string+=l[i]

print sum, string

# print type(l[1])
