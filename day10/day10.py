
# # access list item using loop
# first_list =['apple','ball','banana']
# for item in first_list:
#      print(item,end=",")


# first_list = ['apple', 'ball', 'banana', 'ball', 7, 8, 7]
# second_list = []
# for item in second_list:
#     print(item, end=",")


# list_store
# total_list = []
# print(total_list)

# for i in range(1,6):
#      name = input("enter user name: ")
#      mobile_num = input("enter yout number: ")
#      location = input("enter your location: ")

#      temp_list = []
#      temp_list.append(name)
#      temp_list.append(mobile_num)
#      temp_list.append(location)

#      total_list.append(temp_list)

#      print(temp_list)


# a= 5
# b = 9
# list = []
# print("befor swap value of a is :",a)
# print("befor swap value of b is :",b)


# c = a
# a = b
# b= c
# print("***************")
# print("befor swap value of a is :",a)
# print("befor swap value of b is :",b)
# print(c)


# # without using temp variable
# a,b = b,a


# list = [2,5,6,7,3]
# list_data = []
# for i in list:
#           sq = i*i
#           list_data.append(sq)
# print(list_data)


# list = [2,5,6,7,3]
# list_data =[]
# for i in list:
#      print(i*i)


# list method
data = ['apple', 'ball', 'cat', 5, 9]
print(data.index("cat"))
data.remove("ball")
# data.clear()
# print(data)
second_list = []
second_list = data.copy()
print(second_list)


data = ['f', 'a', 'a', 'f']
data1 = data
data.remove('a')
print(data1)
