# Set a variable that will hold onto the score and set it to zero to start
your_score = 0

# import libraries

import random
import art
import game_data

accounts = game_data.data

# Develop a function for choosing new accounts

def choose_new():
    return random.choice(accounts)


# Develop a function for requesting answers

def request_answer():
   return input("Who has more followers? Type 'A' or 'B': ").upper()

# Create a loop that keeps repeating the new question function until a wrong answer is given. Also add choice "A" or "B"

continue_game = True

your_answer = ""

choice_a = choose_new()
choice_b = choose_new()

while choice_a == choice_b:
    choice_b = choose_new()

while continue_game:
    print(art.logo)
    print(f"Compare A: {choice_a['name']}, {choice_a['description']}, {choice_a['country']}")
    print(art.vs)
    print(f"Against B: {choice_b['name']}, {choice_b['description']}, {choice_b['country']}")

    your_answer = request_answer()

    a_followers = choice_a['follower_count']
    b_followers = choice_b['follower_count']

    is_correct = ((your_answer == "A" and a_followers > b_followers) or (your_answer == "B" and b_followers > a_followers))

    if is_correct:
        your_score += 1
        print(f"You're right! Current score: {your_score}")

       # Determine the winner (correct answer) and loser (the one with the fewer followers)
        if a_followers > b_followers:
            #A was correct; replace A
            choice_a = choose_new()
            while choice_a == choice_b:
                choice_a = choose_new()
        else:
            #B was correct; replace B
            choice_b = choose_new()
            while choice_b == choice_a:
                choice_b = choose_new()


    else:
        print(f"Sorry, that's wrong. Final score: {your_score}")
        continue_game = False





