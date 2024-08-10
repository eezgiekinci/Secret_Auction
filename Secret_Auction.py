# Ask the user for input

# Save the data into a dictionary {name:price}

# Wheather there are other users who want to bid

# Compare the bids and print the winner
bids = {}
continue_bidding = True

def compare_bids(bids):
  winner = ""
  highest_bid = 0
  for bidder_name in bids:
    bid_amount = bids[bidder_name]

    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder_name

  print(f"The winner is {winner} with a bid of ${highest_bid}")

while (continue_bidding):
  name = input("What is your name?\n")
  price = int(input("What is your bid?\n$"))
  bids[name] = price
  other_users = input("Are there any other bidders? Type 'yes'or 'no'\n")

  if (other_users == 'no' ):
    continue_bidding = False
    compare_bids(bids)
    