# Multiples
Part I
for i in range(1,1000):
    if i%2 != 0:
        print i

# Part II
for i in range(5,1000000):
    if i%5 == 0:
        print i


# Sum List
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum+=i
print sum


# Average List
a = [1, 2, 5, 10, 255, 3]
sum = 0
count = len(a)
for i in a:
    sum+=i
print sum/count
