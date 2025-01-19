# name = "roshan"
# for letter in name:
#     full_letter ="@"+letter
#     print(full_letter)

# num = 5
# a = 6.5
first_data = ["apple", "ball", "dog"] #list
list=[]
for list in first_data:
    full_list = "it is " +list 
    print(full_list)

first_data = ["apple", "ball", "dog"] #list
for item in first_data:
    sentence = "it is "+" a " + item
    print(sentence)

first_data = ["apple", "ball", "dog"] #list
for item in first_data:
    if item[0] in "aeiou":
        output = "an"
    else:
        output = "a"
    sentence = "it is "+ output + " " + item
    print(sentence)

# range(start,stop,step)
# step
# range(5,10)

for i in range(1,100):  #print 1 to 100
    print(i)    

for i in range(1,200,2): # print 1 to 3 print
    print(i)

for i in range(18,40): # print 19 to 39
    print(i)

for i in range(0,100):   # print odd even number in 100
    if i%2==0:
        print("even",i)
    else:
        print("odd",i)

for i in range(50,5,-1): #print 50 to -5 
        print(i)

import random

random_number = random.randint(1,100)
print(random_number)


name = "tribhuvanuniversity"
print(len(name))
for i in range(18,-1,-1):
    print(name[i])


name = "tribhuvanuniversity"
print(name[18:0:-1])


for i in range(1,6):
    for j in range(1,6):
      print(i,j)

for fruit in ["apple", "banana"]:
   for animal in ["cat","dog"]:
        print(fruit,animal)

for i in "AB":
    for j in "CD":
        print(i,j)


for i in range(1,6): #star making
    for j in range(i):
        print("*",end="")
    print("")


for i in range(6,1,-1): #6 to 1 star making
    for j in range(i):
        print("*",end="")
    print("")