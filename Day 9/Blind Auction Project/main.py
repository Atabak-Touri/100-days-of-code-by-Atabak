from art import logo
# TODO-1: Ask the user for input

# # TODO-2: Save data into dictionary {name: price}



# bids = {}
# bids[name] = price
# TODO-3: Whether if new bids need to be added
def highest_bid():
    for
dictionary={}
other_player=input("is there other player?")
continue_biding = True
while continue_biding:
    name = input("What is your name?")
    bid = int(input("How much you want to bid?"))
    dictionary[name]=bid
    others=input("is there any other palyer?")
    if others == "no":
        continue_biding= False
        highest_bid(bid)
    else:
        continue_biding=True

# should_continue=input("is there any other person? yes or no?\n")
#
# continue_bidding = True
# while continue_bidding:
#     name =input("What is your name?: ")
#     price= int(input("What is your bid?: $"))
#     bids[name]= price
#     should_continue = input("is there any other person? 'yes' or 'no'?\n").lower()
#     if should_continue == "no":

# TODO-4: Compare bids in dictionary

# def find_highest_bidder(bidding_dictionary):
#     highest_bid = 0
#     for bidder in bidding_dictionary:
#         bid_amount = bidding_dictionary[bidder]
#         if bid_amount>highest_bid:
#             highest_bid = bid_amount
#             winner= bidder
#     print(f"the binner is {winner}, with a bid of ${highest_bid}.")
