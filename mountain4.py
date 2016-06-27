#Mountains 4
dictionary = {"mount everest": {"elevation": 8848, "range": "himalayas"}, "k2": {"elevation": 8611, "range": "Himalayas"}, "kangchenjunga":{"elevation": 8586, "range": "himalayas"}, "Lhotse": {"elevation": 8516,\
"range": "himalayas"}, "Makalu": {"elevation": 8462, "range": "himalayas"}}


for mountain in dictionary:
    print(mountain.title())


for mountain in dictionary:
    print(dictionary[mountain]["elevation"])


for mountain in dictionary:
    print(dictionary[mountain]["range"].title())


for mountain in dictionary:
    print("%s is an %d-meter tall mountain in the %s." % (mountain.title(), dictionary[mountain]["elevation"],(dictionary[mountain]["range"]).title()))
