def persons_name(name):

    print("Hello, %s!" % name.title())
    print("How are you, %s?" % name.title())
    print("It's great to see you again, %s!\n" % name.title())

list_of_names = ["Tarun", "Vikul", "Leonardo"]
for name in list_of_names:
    persons_name(name)
