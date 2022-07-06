
import os
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

bids = {}

bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for user in bidding_record:
        bid_amount = bidding_record [user]
        if bid_amount > highest_bid:
            highest_bid = bidding_record[user]
            winner = user
    print(f"\nThe winner is {winner} with the bid of ${highest_bid}.")

while not bidding_finished:
  name = input("What's your name: ")
  price = float(input("What's the bid? $"))
  
  bids[name] = price
  
  should_continue = input("Another user? 'yes' or 'no'\n").lower().strip()[0]
  
  if should_continue == "n":
    bidding_finished = True
    find_highest_bidder(bids)
  else:
    os.system("clear")
