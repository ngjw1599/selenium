# product_type = {'Fitness Wear': ["Sports Bra", "Yoga Pants"],
#                 'Resistance Bands' : ["Hip Bands", "Multi Resistance Bands"],
#                 'Skipping Rope': ["Skipping Rope", "Digital Skipping Rope"]}


# column_names = ["Category", "Type"]
# #create list 
# list_of_info = []

# for main_type in product_type:
#     for item in product_type[main_type]:
#         dict_data = {
#                         "Category": main_type,
#                         "Type": item
#                         }
#         list_of_info.append(dict_data)

# print(list_of_info)

number_set = [1234567890]

[1, 2, 5, 6, 8, 9, Ellipsis]

before = ['1', '2', '...', '11', '12', '14', '15', '...', 'See All ']
after = ['1', '2', '...', '13', '14', '16', '17', '...', 'See All ']
before.pop()
for i in before:
    if i.isdigit() != True:
        before.remove(i)

before = [eval(i) for i in before]

print(max(before))


