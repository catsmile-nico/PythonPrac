# https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
## If n is odd, print Weird
## If n is even and in the inclusive range of 2 to 5, print Not Weird
## If n is even and in the inclusive range of 6 to 20, print Weird
## If n is even and greater than 20, print Not Weird

## Sample Input 1
## 24
##
## Sample Output 1
## Not Weird

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    if(n%2!=0 or (n>=6 and n<=20)):
        print("Weird")
    else:
        print("Not Weird")

