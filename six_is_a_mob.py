#Six is a mob
names = ["Louis", "Vikul", "Tarun", "Leonardo", "Francisca", "Chiara"]

def crowd(names):
    if(len(names)>5):
        print("There is a mob in the room")

    if(len(names)>=3):
        print("The room is crowded")

    if(len(names)>=1):
        print("The room is not crowded")

    else:
        print("The room is empty")

crowd(names)
