import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players")
    else:
        print("Invalid, try agin.")

max_score = 50
player_scores = [0 for _ in range(players)]


while max(player_scores) < max_score:
    for player_index in range(players):
        print("\nPlayer", player_index + 1,"'s turn has just started!")
        print("Your total score is:", player_scores[player_index],"\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ").lower()
            if should_roll != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:",value)
            
            print("your score is:", current_score)

        player_scores[player_index] += current_score
        print("Your total score is:", player_scores[player_index])
    
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx+1, "is the winner with a score of",max_score,"!")
