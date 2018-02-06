import random

def coinTosses():
    toss = random.randint(0,1)
    print "Starting the program"
    head = 0
    tail = 0
    result = ""
    for i in range(1,5001):
        toss = random.randint(0,1)
        if toss == 1:
            head+=1
            result = "head"
        elif toss == 0:
            tail+=1
            result = "tail"
        print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far".format(i,result,head,tail)
print "Ending the program, thank you!"

coinTosses()
