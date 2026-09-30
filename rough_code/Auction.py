def find_highest_biding(bidding_dictionary):
    winner=""
    highest_bid=0
    max(bidding_dictionary)
    for bidder in bidding_dictionary:
        biding_amount=bidding_dictionary[bidder]
        if biding_amount > highest_bid:
            highest_bid=biding_amount
            winner=bidder
    print(f"the winner is {winner} with the bid ${highest_bid}")

bids={}

continue_biding=True
while continue_biding:
    name = input("what is you name?: ")
    price = input("what is your bid?: $")
    bids[name] = price
    should_continue = input("Are there any other biders? type 'yes' or 'no' \n")
    if should_continue == "no":
        continue_biding = False
        find_highest_biding(bids)
    elif should_continue == "yes":
        print("\n" * 20)





