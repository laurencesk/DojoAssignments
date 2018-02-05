list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

lenList1 = len(list_one)
lenList2 = len(list_two)
identical = 0

if lenList1 == lenList2:
    for i in range(0,lenList1):
        if list_one[i] == list_two[i]:
            identical+=1
    if identical == lenList1:
        print "They are identical"
    else:
        print "They are not identical"
else:
    print "They are not identical"
