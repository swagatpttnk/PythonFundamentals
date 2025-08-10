import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(list(range(22)), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}}
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)
numbers_matched = [
    {"matchlen":len(lottery_numbers.intersection(player["numbers"])),"name":player["name"] } for player in players
]
print(lottery_numbers)
print(numbers_matched)
winnerIndex=0
maxCount=0
for counter,mt in enumerate(numbers_matched):
    if mt["matchlen"] > maxCount :
        winnerIndex = counter
        maxCount = mt["matchlen"]
winner = numbers_matched[winnerIndex]["name"]
winning_prize = 100 ** numbers_matched[winnerIndex]["matchlen"]
print(f"Winner is { winner }")
print(f"{winner} won { winning_prize }")