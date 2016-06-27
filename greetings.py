def persons_name(name):

    print("Hi, %s!" % name.title())
    print("Whats the craic, %s?" % name.title())
    print("I'll see you later, %s!\n" % name.title())

list_of_names = ["Tarun", "Vikul", "Leonardo"]
for name in list_of_names:
    persons_name(name)
