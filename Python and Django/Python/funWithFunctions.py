def odd_even():
    for i in range(1,2001):
        if i % 2 ==0:
            print str(i)+' is even'
        else:
            print str(i)+' is odd'
odd_even()



def multiply(arr,num):
    for i in range(0,len(arr)):
        arr[i] = arr[i]*num
    return arr

multiply([2,4,10,16],5)



def layered_multiples(arr,num):
    newArr1 = multiply(arr,num)
    newArr2 = []
    newArr3 = []
    for i in range(0,len(newArr1)):
        newArr2 = []
        for j in range(0,newArr1[i]):
            newArr2.append(1)
        newArr3.append(newArr2)
    print newArr3

layered_multiples([2,4,5],3)
#
