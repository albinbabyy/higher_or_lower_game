from game_data import data
import random


def format_data(account):
    # formating  the account data into printable form.
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_descr}, {account_country}"

# Creating a random account from the game data

account_a = random.choice(data)
account_b = random.choice(data)
# in any case account a and b become equal to solve that,
if account_a == account_b:
    account_b = random.choice(data)

print(f"comapare A: {format_data(account_a)}")
print(f"comapare B: {format_data(account_b)}")