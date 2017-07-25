#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays, compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

#Remember the rules:

#Rock beats Scissors
#Scissors beats paper
#Paper beats rock


user_1_play = raw_input("User 1: Would you like to play a game? Type y for YES or n for NO: ") #input determining whether player wants to play. input for initial function
user_2_play = raw_input("\nUser 2: Would you like to play a game? Type y for YES or n for NO: ")

def game_initialize(input1, input2): #this function determines whether the players will play or not
  if input1 and input2 == "y":
    game_logic()
  else:
    print "No game today"

def game_logic():
  user_1_move = raw_input("\nUser 1: Choose rock, paper, and or scissors: ").lower()
  user_2_move = raw_input("\nUser 2: Choose rock, paper, and or scissors: ")
  game_actual(user_1_move, user_2_move).lower()

def game_actual(user1, user2):

    if (user1 == "rock" and user2 == "scissors") or (user1 == "paper" and user2 =="rock") or (user1 == "scissors" and user2 == "paper"):
        print "User 1, you win!"
    if user1 == user2:
        print "It's a tie!"
    else:
        print "User 2, you win!"


game_initialize(user_1_play, user_2_play)
