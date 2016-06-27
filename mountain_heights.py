#Mountain heights
world_mountains = {"Mount Everest" : 8848, "K2" : 8611,"Kangchenjunga" : 8586, "Lhotse" : 8516, "Makalu" : 8462}

for k in world_mountains:
    print(k)

for v in world_mountains:
    print(world_mountains[v])

for k,v in world_mountains.items():
    print(k+" "+ v)
