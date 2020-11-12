#Choose your own adventure game//practice

print("Welcome to the game!")
name = input("What is your name? ")
age = int(input("What is your age? "))


health = 10

if  age >= 18:
    print("Welcome", name, "you are old enoungh to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's PLAY!")
        print("You are starting with", health, "health.")
        left_or_right = input("First choice....Left or Right? (left/right) ").lower()
        if left_or_right == "left":
            ans = input("Nice, you follow a path and reach a lake... Do you swim"  
            " across or go around? (swim/around)").lower
            if ans == "around":
                print("You went around and reached the other side of the lake")
            elif ans == "swim":
                print("You managed to swim across but got bit by a fish and lost 5 health")
                health = health - 5
            

            ans = input("You notice a house and a river feeding the lake. Which do you go to?"
                       " (river/house) ").lower()
            if ans == "house":
                print("You go to the house and are greated by the owner...He isn't happy.")
                print("You get hit and lose 5 health")
                health = health - 5;
                if health <= 0:
                    print("You have no health left and are a corpse.")
            else:
                print("You fell in the river and drowned. The current was to strong!")
                health = 0
                if health <= 0:
                    print("You have no health left and are a corpse.")
        else:
            print("You fell down a giant hole...")
            health = 0
            if health <= 0:
                    print("You have no health left and are a corpse.")
    else:
        print("Oh...okay...good bye then... :( ")

else:
    print(name, "you are not old enough to play...Sorry!")
