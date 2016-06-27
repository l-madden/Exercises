#Mountains 3
highest_mountains = {'Mount Everest': 8848, 'K2': 8611, 'Kangchenjunga': 8586, \
'Lhotse': 8516, 'Makalu': 8462}

highest_mountains_dictionary = {'Mount Everest': [8848], 'K2': [8611], 'Kangchenjunga': [8586], \
'Lhotse': [8516], 'Makalu': [8462]}

def feet_conversion(elevation):
    return elevation*3.28

for mountain in highest_mountains:
   
    elevation_to_feet = feet_conversion(highest_mountains[mountain])
    print("%d m equals %d feet." % (highest_mountains[mountain], elevation_to_feet))
    highest_mountains_dictionary[mountain].append(elevation_to_feet)


for mountain in highest_mountains_dictionary:
    print(mountain)


for mountain in highest_mountains_dictionary:
    print(highest_mountains_dictionary[mountain][0])


for mountain in highest_mountains_dictionary:
    print("%.2f" % highest_mountains_dictionary[mountain][1])


for mountain in highest_mountains_dictionary:
    print("%s is %d meters tall, or %.2f feet." % (mountain,\
highest_mountains_dictionary[mountain][0], highest_mountains_dictionary[mountain][1]))
