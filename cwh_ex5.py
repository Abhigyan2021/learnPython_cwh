
# Constructing a Snake, Water,Gun Game

import random

name = input("Welcome! Please input your Name: ")

print("Hello,", name, ". Let's play Snake Water and Gun.")

print("Rules of GAME:\n1)Player will select one between Snake Water and Gun.\n2)Snake beats Water, Water beats Gun, Gun beats Snake.\n3)Press '0' for snake, '1' for Water, '2' for Gun.\n4)Press 'q' to quit.")
print("Let's Play!!!")

p_scr = 0
c_scr = 0

def winner(p_scr, c_scr):
    if p_scr == c_scr :
      print("Match is a Draw!")
    elif p_scr > c_scr:
      print(f"Congratulations {name}!! You have won the game.")
    else:
      print("Sorry {name} !! You've lost the game.")


points = [[0,1,-1],[-1,0,1],[1,-1,0]]

while(True):

    lst1 = [0,1,2]
    dict1 = {0 : "Snake", 1 : "Water", 2 : "Gun"}

    key1 = int(input("Enter your Move(9 for quit):"))
    key2 = int(random.choice(lst1))

    if(key1 == 9):
        winner(p_scr, c_scr)
        break
    
    print("Player Chose : ", dict1[key1])
    print("Computer Chose : ", dict1[key2])
    if points[key1][key2] == 0:
       print("This hand is a draw!")
    elif points[key1][key2] == 1 : 
       print("Player Wins this hand!")
    else:
       print("Computer Wins this hand!!")

    if(key1 != key2):
       p_scr = p_scr + points[key1][key2]
       c_scr = c_scr + points[key2][key1]

    




