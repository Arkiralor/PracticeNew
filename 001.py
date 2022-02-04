'''
If there is a string that is 'python3code7program5'
'''

# inp = 'python3code7program5'

# num_list = max([i for i in inp if i.isdigit()])

# print(num_list)

# max = 0
# max_list = []

# for item in num_list:
#     if int(item)>max:
#         max = item
#         num_list.pop(item)
#         max_list.append(max)
#         max = 0

# print(max_list)

# SELECT Employee_Name from Employee WHERE Employee_Name = 'A*';
    
let_list = ['a', 'b', 'c']
let_dict = {}


for i in range(len(let_list)):
    # temp_dict = {i: let_list[i]}
    let_dict = {**{i: let_list[i]},**let_dict}
print(let_dict)

# for index, value in range(enumerate(let_list)):
#     word_dict = {**{index: value}}

# print(word_dict)
