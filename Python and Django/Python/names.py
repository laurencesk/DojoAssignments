# Part I
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def partI(arr):
    for i in range(0,len(arr)):
            print "{}{}".format(arr[i]['first_name'],arr[i]['last_name'])

partI(students)

#Part II

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def partII(arr):
    print "Students"
    for i in range(0,len(arr["Students"])):
            strLen = len(arr["Students"][i]['first_name'])+len(arr["Students"][i]['last_name'])
            print "{}{}{}{}".format(i+1,arr["Students"][i]['first_name'],arr["Students"][i]['last_name'],strLen)
    print "Instructors"
    for i in range(0,len(arr["Instructors"])):
            strLen = len(arr["Students"][i]['first_name'])+len(arr["Students"][i]['last_name'])
            print "{}{}{}{}".format(i+1,arr["Instructors"][i]['first_name'],arr["Instructors"][i]['last_name'],strLen)
partII(users)
