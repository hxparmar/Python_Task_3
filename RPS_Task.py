# Implement a Text-Based Rock, Paper, Scissors Game
#Objective: Create a simple text-based Rock, Paper, Scissors game that allows a user to play against the computer. The game should handle user input, computer moves, and determine the winner based on the standard rules.
#Implement a function play( ) which  should contain the user's choice and the computer's choice and returns the result of the game ("win", "lose", or "tie").
#Ensure that the game handles invalid input gracefully (e.g., if the user enters something other than "rock", "paper", or "scissors").


import random
d=["Rock","Paper","Scissors"]
u=0
s=0
def play():
    global d,u,s
    def task():
        global d,u,s
        print("************************************************\n")
        print("              ROCK PAPER SCISSORS!!!!!          \n")
        print("************************************************\n")
        disp=print("This game is called Rock Paper and Scissors!\nThere are some rules to be followed for the users to.\nThe following are the rules for the gamers to know inorder to win the game!!\nRULES:\n1. Rock vs Paper---> Paper wins!\n2.Scissors vs Rock---> Rock wins!\n3.Paper vs Scissors---> Scissors wins!\n")
        i=0
        while i<5:
            global d,u,s
            user=input("ROCK PAPER SCISSORS!!!!:")
            machine=random.choice(d)
            print("The System gives:",machine)
            if user=='Rock' and machine=='Paper':
                print("Rock against Paper...Paper wins!!!")
                print("Gamer LOSES")
                s+=1
                u+=0
            elif user=='Rock' and machine=='Scissors':
                print("Rock against Scissors...Rock wins!!!")
                print("Gamer WINS")
                s+=0
                u+=1
            elif user=='Rock' and machine=='Rock':
                print("Rock against Rock...DUD!!!")
                print("ITS A TIE...")
                s+=0
                u+=0

            elif user=='Paper' and machine=='Rock':
                print("Paper against Rock...Paper wins!!!!!!")
                print("Gamer WINS")
                s+=0
                u+=1
            elif user=='Paper' and machine=='Scissors':
                print("Paper against Scissors...Scissors wins!!!")
                print("Gamer LOSES")
                s+=1
                u+=0
            elif user=='Paper' and machine=='Paper':
                print("Paper against Paper...DUD!!!")
                print("ITS A TIE...")
                s+=0
                u+=0

            elif user=='Scissors' and machine=='Rock':
                print("Scissors against Rock...Rock wins!!!")
                print("Gamer LOSES")
                s+=1
                u+=0
            elif user=='Scissors' and machine=='Paper':
                print("Scissors against Paper...Scissors wins!!!")
                print("Gamer WINS")
                s+=0
                u+=1
            elif user=='Scissors' and machine=='Scissors':
                print("Scissors against Scissors...DUD!!!")
                print("ITS A TIE...")
                s+=0
                u+=1

            elif user not in ['Rock','Scissors','Paper','exit'] and machine=='Rock':
                print("Invalid.Try again")
                s+=0
                u+=0
            elif user not in ['Rock','Scissors','Paper','exit'] and machine=='Paper':
                print("Invalid.Try again")
                s+=0
                u+=0
            elif user not in ['Rock','Scissors','Paper','exit'] and machine=='Scissors':
                print("Invalid.Try again")
                s+=0
                u+=0
            
            elif user=='exit':
                print("The total scores of the gamer is",u,".The total score of our system is",s)
                if u>s:
                    print("GAMER WON THIS ROUND!!!!")
                elif u<s:
                    print("GAMER LOSES THIS ROUND!!!!")
                elif u==s:
                    print("THIS ROUND ENDS IN TIE!!!!!")
                print("\nEXITING THE GAME")
                break
            elif i==4:
                print("The total scores of the gamer is",u,".The total score of our system is",s)
                if u>s:
                    print("GAMER WON THIS ROUND!!!!")
                elif u<s:
                    print("GAMER LOSES THIS ROUND!!!!")
                elif u==s:
                    print("THIS ROUND ENDS IN TIE!!!!!")  
            i+=1
    task()
play()
        
                

                
    

























































