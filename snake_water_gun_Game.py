player1=input(f"Player 1 Enter a character  For snake (s) and for water (w) and for Gun (g) ??\n")
player2=input(f"Player 2 Enter  a character Number For snake (s) and for water (w) and for Gun (g) ??\n")
if player1==player2:
    print("Tie")
elif player1=="s":
    if player2=="w":
        print("player1 win")
    elif player2=="g":
        print("player2 win")

elif player1=="w":
    if player2=="s":
        print("player2 win")
    elif player2=="g":
        print("player1 win")
elif player1=="g":
    if player2=="s":
        print("player1 win")
    elif player2=="w":
        print("player2 win")
else:
    print("please select any one option from above")


print(f"player one is enter :{player1}")
print(f"player second  is enter :{player2}")