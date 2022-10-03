product_type = {'Fitness Wear': ["Sports Bra", "Yoga Pants"],
                'Resistance Bands' : ["Hip Bands", "Multi Resistance Bands"],
                'Skipping Rope': ["Skipping Rope", "Digital Skipping Rope"]}

for main_type in product_type:
    print(main_type)
    for item in product_type[main_type]:
        print(item)