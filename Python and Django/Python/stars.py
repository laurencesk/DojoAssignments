# Part I

def draw_stars(arr):
    for i in range(0,len(arr)):
        print ("*"*arr[i])

draw_stars([4, 6, 1, 3, 5, 7, 25])


# Part II
def draw_stars(arr):
    for i in range(0,len(arr)):
        if isinstance(arr[i],int) == True:
            print ("*"*arr[i])
        elif isinstance(arr[i],str) == True:
            print (arr[i][0].lower())*len(arr[i])


draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
