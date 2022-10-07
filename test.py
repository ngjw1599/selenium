product_type = {'Fitness Wear': ["Sports Bra", "Yoga Pants"],
                'Resistance Bands' : ["Hip Bands", "Multi Resistance Bands"],
                'Skipping Rope': ["Skipping Rope", "Digital Skipping Rope"]}


column_names = ["Category", "Type"]
#create list 
list_of_info = []

for main_type in product_type:
    for item in product_type[main_type]:
        dict_data = {
                        "Category": main_type,
                        "Type": item
                        }
        list_of_info.append(dict_data)

print(list_of_info)