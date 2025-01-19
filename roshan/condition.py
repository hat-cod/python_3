# condations = nepali ma (yadi)
# type of condition
# if,if...else,if...elif....elif...elif...else( nested condition)

# age = 19
# if age>18:
    # print("you are young")

# syntax:
# if condition teue:
    # statement

# age = 5
# if age>20:
#     print("you are a marry")
# if age<18:
#     print("you are not marry")


# age = 30
# if age>25:
#     print("your yong")
# if age<18:
#     print("you are teen age")



# age = 50
# if age>60:
#     print("you are old")
# else:
#     print("you are young")


# # wap to output like child,adult,old

# age = 2
# if age>=15:
#     print("you are child")
# if age>=30:
#     print("you are young")
# else:
#     print("you are old")


# age = -13

# if age>0 and age<13:
#     print("you are child")
# elif age>=13 and age<20:
#     print("you are teenagers")
# elif age<0 or age>200:
#     print("wrong input")
# else:
#     print("either you are adult or old")

# age = 12
# if age>0:
#     print("you are child")
# if age<17:
#     print("you are teenagers")



# age = 45
# if isinstance(age,str) and age.isdigit() == False:
#     print("invalid age") #if not age.isdigit()
# elif age>0 and age<13:
#     print("you are child")
# elif age>=13 and age<20:
#     print("you are teenagers")
# elif age<0 or age>200:
#     print("invlade age")
# else:
#     print("your adult and old")


# # /* user input */
# # input() - > string

# age = input("enter your age:-")
# # print("your age is",age)
# age = int(age)
# if isinstance(age,str) and age.isdigit() == False:
#     print("invalid age") #if not age.isdigit()
# elif age>0 and age<13:
#     print("you are child")
# elif age>=13 and age<20:
#     print("you are teenagers")
# elif age<0 or age>200:
#     print("invlade age")
# else:
#     print("your adult and old")


# print("Enter thr mark of the student")
# marks = input()

# if not marks.isdigit():
#     print("Invlade pleace enter the number:")


# else:
#     marks=int(marks)

#     if(marks>=90):
#         grade="A"
#     elif(marks<90 and marks>=80):
#         grade="B"
#     elif(marks<80 and marks>=70):
#         grade="C"
#     elif(marks<70 and marks>=32):
#         grade="D"
#     else:
#         geade="F"

#     print("The Grade Obtain By Studen is:",grade)


# #    */odd number and even number ?*

#     num = int(input("enter num:-"))
#     if num%2==0:
#         print("even")
#     else:
#         prin("odd num")

    # prime number ?
    # pusdo code

# num = int(input("enter number:- "))
# start = 1
# num =2
# remaind = num%2
# if remaind ==0:
#     cont = cont+1
# if start<=num:
# if count>2:
#     print("it is composite num")
# else:
#     print("it is prime num")
i = 0
# num = int(input("enter num:-"))
start = int(input("enter start number:-"))
end = int(input("enter end number"))
for num in range(start, end +1):
        if num % 2 == 0:
           print("even",num)
        else:
            print("odd",num)



#creat a start input  start and end 
start = int(input("Enter the start : "))
end = int(input("Enter the end : "))

# add count value in count 
count = 0

# creat a loop stetment an value (start,end+1)
for num in range(start, end + 1):
    if num > 1:  # add  varebal  and  end value 1
        prime = True #number is true 
        for i in range(2, num):# add nested loop in add count value and end value
            if num % i == 0:  # Found a divisor is num and count
                prime = False #number is false stetment
                break  # break is do no chack  stament
        
        if prime:  # If the number is prime
            print(f"{num} is a prime number.") #farmiting and num and print
            count += 1  # adding prime number counter

# Output the total count of prime numbers
print(f"Total prime numbers between {start} and {end}: {count}")
