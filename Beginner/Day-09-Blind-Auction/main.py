from replit import clear
from art import logo

def find_highest_bidder(bids):
  highest_bidder = ""
  highest_bid = 0
  for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > highest_bid:
      highest_bidder = bidder
      highest_bid = bid_amount
  print(f"The highest bidder is {highest_bidder} with a price of ${highest_bid}!\n{highest_bidder} wins!")

bids = {}
bidding_finished = False
print(logo)

while not bidding_finished:
  bidder_name = input("Please enter your name: ")
  bid_price = int(input("Please enter your bid price: $"))
  bids[bidder_name] = bid_price
  print(bids)
  
  should_continue = input("Are there other bidders who want to bid?\nType 'yes' or 'no':\n")
  if should_continue == "yes":
    clear()
  elif should_continue == "no":
    find_highest_bidder(bids)
    print("Thank you for participating! Goodbye!")
    bidding_finished = True