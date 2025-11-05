import logo

print("Welcome to the Auction program")


def highest_bid(bidding_dictonary):
    winner = ""
    highest_bid = 0

    max(bidding_dictonary)

    for bidder in bidding_dictonary:

        bid_value = bidding_dictonary[bidder]
        if bid_value > highest_bid:
            highest_bid = bid_value
            winner = bidder
    print(f"\nThe winner of the auction is {winner}"
          f"\nWith the bid value of ${highest_bid}\n")



bidding ={}
other = True
while other:
    name = input("what is your name? ")
    price = int(input("what is your bid?  "))
    bidding[name] = price
    other_option = input("what is your other bidder? Type'yes' or 'no'\n ").lower()

    if other_option == "no":
        other = False
        highest_bid(bidding)

    elif other_option == "yes":
        print("\n"*50)
