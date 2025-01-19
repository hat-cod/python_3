# superset = "abcd"


# for i in superset:
#     print(i)
#     for j in superset:
#         print(i,j)
#         for k in superset:
#             print(i,j,k)
#             for l in superset:
#                 print(i,j,k,l)


# for i in range(10):
#     print(i)
#     if i ==4:
#         break

# for i in range(10):
#     if i ==4:
#         continue
#     print(i)

# for i in range(10):
#     pass

# os
# import os 
# os.mkdir("roshan") # make folder
# print("you are dir:",os.getcwd()) # checck directy in folder
# a = os.lidtdir(os.gercwd()) # go to folder
# print(a)

# specify the directory
directory_path = "G://"
# walk through the directory
for dirpath, dirnames, filenames in os.walk(directory_path):
    print(f"Current Directory: {dirpath}")
    print(f"Subdirectories: {dirnames}")
    print(f"files: {filenames}")
    print("-" * 40)


first_list