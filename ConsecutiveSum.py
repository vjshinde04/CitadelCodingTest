# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
# #
# # Complete the 'consecutive' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts LONG_INTEGER num as parameter.
# #
#
# def consecutive(num):
#     # Write your code here
#
# if __name__ == '__main__':

def consecutive(num):
    # Write your code here
    i = 1
    sumnum = count = 0
    sumArray = []
    for i in range(1,num):
        sumnum = sumnum + i
        sumArray.append(i)
        print('{} : {}'.format(i, sumnum))
        if sumnum == num:
            count += 1
            print(sumArray)
            sumnum = 0


    # return (count)

consecutive(21)