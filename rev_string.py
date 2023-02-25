'''
Script to reverse a string
'''


s:str = 'I love India'

# s_list = [i for i in s]
# s_list.reverse()
# new_string = ''.join(s_list)
# print(new_string)

# s_list = s.split()
# word = s_list[-1]
# # print(word)
# word_list = [letter for letter in word]
# word_list.reverse()
# new_word = ''.join(word_list)
# s_list[-1] = new_word
# sentence = ' '.join(s_list)

# print(sentence)
# s_list = [i for i in s]
# # print(s_list)
# count_of_letter = 0

# for j in range(len(s_list)):
#     if s_list[j] == 'I' or s_list[j] == 'i':
#         count_of_letter = count_of_letter + 1

# print(f"The count of 'i': {count_of_letter}")

a = [0, 5, 7, 8, 100, ' ']

count_of_num = 0

for item in a:
    if type(item) == int:
        count_of_num = count_of_num + 1

print(count_of_num)
