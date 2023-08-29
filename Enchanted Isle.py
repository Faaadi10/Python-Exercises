print ("Enchanted Isle")
print ("You've to find and rescue a child")
choice1 = input("you've come at a crossroad, where do you want to go? letf or right?\n").lower()
if choice1 == "right":
    choice11 = input ("you've arrived at a lake. Type Wait to wait or type swim as next step\n").lower()
    if choice11 == "wait":
        choice111 = input("You arrived at the island, now you get to see house with 3 doors of red, yellow and blue colour. Which one would You choose?\n").lower()
        if choice111 == "red":
            print("game over")
        elif choice111 == "yellow":
            print ("game over")
        else:
            print ("you won the game")

    else:
        print("You were attacked by some sort of aquatic animal. Sorry, you lost")

else:
    print("game over")
