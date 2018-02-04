l = ['magical unicorns',19,'hello',98.98,'world']

sum = 0
string =""

for i in range(0,len(l)):
    if type(l[i]) is int or type(l[2]) is float:
        sum+=l[i]

    elif type(l[i]) is str:
        string+=l[i]

print sum, str

# print type(l[1])
