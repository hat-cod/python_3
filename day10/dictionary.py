# user_data = {}
# user_data_detail = {'name': 'roshan', 'location': 'jkt'}
# # print(user_data_detail["name"])
# user_data_detail["name"] = "ram"
# for key in user_data_detail:
#     print(user_data_detail[key])


user_data = {}
user_data_detail = {"name": "roshan", "num": "9878"}
# for value in user_data_detail:
    # print(user_data_detail)
    
    
for key in user_data_detail:
    if key == ["number"] :
        user_data_detail[key] = "+977" + user_data_detail[key]
print(user_data_detail)
