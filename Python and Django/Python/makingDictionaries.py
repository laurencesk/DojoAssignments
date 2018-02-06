name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def makingDictionaries(arr1,arr2):
    dic = dict(zip(arr1,arr2))
    print dic

makingDictionaries(name,favorite_animal)
