# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
# # Complete the 'getUnallottedUsers' function below.
# #
# # The function is expected to return an INTEGER_ARRAY.
# # The function accepts following parameters:
# #  1. 2D_INTEGER_ARRAY bids
# #  2. INTEGER totalShares
# #
# def getUnallottedUsers(bids, totalShares):
#     # Write your code here
#     # <userId, noShares, biddingPrice, timeStamp>
#     # print(bids)
#
# if __name__ == '__main__':


# 3
# 4
# 1 2 5 0
# 2 1 4 2
# 3 5 4 6
# 3
# output = 3

def getUnallottedUsers(bids, totalShares):
    countBidders = len(bids)
    dictBid = {}
    for i in range(countBidders):
        # print(bids[i][2])
        # print(bids[i][1])
        # {userId:bidderPrice}
        dictBid.update({bids[i][0]: bids[i][2]})
    # print(dictBid)
    # print(sorted(dictBid.values(), reverse = True))
    dictBidSorted = dict(sorted(dictBid.items(), key=operator.itemgetter(1), reverse=True))
    print(dictBidSorted)
    for item in dictBidSorted:
        item.key



