highest_mountains = {'Mount Everest': 8848, 'K2': 8611, 'Kangchenjunga': 8586, \
'Lhotse': 8516, 'Makalu': 8462}

for mountain in sorted(highest_mountains):
    print("%s is %d meters tall." % (mountain, highest_mountains[mountain]))
