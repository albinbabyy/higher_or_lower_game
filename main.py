from game_data import data
import random


def format_data(account):
    # formating  the account data into printable form.
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name},\n {account_descr}, {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and followers counts and return if they got right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

score = 0

# for game repeating
game_should_continue = True

account_b = random.choice(data)

while game_should_continue:
# Creating a random account from the game data

    account_a = account_b
    account_b = random.choice(data)
    # in any case account a and b become equal to solve that,
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"comapare A: {format_data(account_a)}")
    print(f"comapare B: {format_data(account_b)}")

    guess = input("Who has more followers \Type 'a' or 'b' : \n")

    # followers count of each account

    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]
    # check if the user is correct
    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    # give feed back on their guess and score keeping
    if is_correct:
        score +=1
        print(f"you are right, current score : {score}")
    else:
        game_should_continue = False
        print(f"sorry, thats wrong, final score:{score}")
