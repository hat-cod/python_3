# type of loop 
# for loop,while loop, nested loop

# name = True 
# i = 0 
# while name:
#     print("roshan")
#     if i == 100:
#         name = False 
#     i=i+1

# # class work
# i=1
# while i<=50:
#     if i%2==0:
#         print("even",i)
#     else:
#         print("odd",i)
#     i=i+1

num=2
count = 0
start = 1
while start<=num:
    if num%start==0:
        count = count + 1
    start = start +1
if count<=2:
    print(f"{num} is prime number")