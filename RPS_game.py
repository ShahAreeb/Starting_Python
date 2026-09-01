import random
choices=["Rock","Paper","Scissor"]
player_score=0
comp_score=0
while True:
    print("\n 1.Rock")
    print("\n 2.Paper")
    print("\n 3.Scissor")
    print("\n 4.Exit")

    choice=int(input("Choose : "))

    if choice==4:
        break
    elif choice>4 or choice<1:
        print("Invalid Option")
        continue

    computer=random.choice(choices)
    player=choices[choice-1]

    if computer==player:
     print("Tied , try again")
    elif (computer=="Rock" and player=="Paper")or (computer=="Paper" and player=="Scissor") or (computer=="Scissor" and player=="Rock"):
      print("You won this game")
      player_score+=1
      print("Your Score:",player_score)
      print("Computer's Score:",comp_score)
    else:
      print("Computer Won")
      comp_score+=1
      print("Your Score:",player_score)
      print("Computer's Score:",comp_score)
    