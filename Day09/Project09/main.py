from asciiLogo import logo

print(logo)

list_bidders = {}
while True:
    print("\nWelcome to the secret auction program.")
    name = input("What is your name?: ")
    bidPrice = float(input("What's your bid?: $"))
    list_bidders[name] = bidPrice
    othersBidders = input("Are there any other bidders? Type 'yes' or 'no': ")
    if othersBidders == "yes":
        continue
    elif othersBidders == "no":
        break
    else:
        print("\nPlease insert a valid option!")

highest_bid = max(list_bidders.values())
print("\nBidders and their bids:")

for bidder, bid in list_bidders.items():
    if bid == highest_bid:
        print(f"The winner is {bidder}with a bid of ${bid}")
