# https://www.hackerrank.com/challenges/input/problem?isFullScreen=true

# Sample Input
# 1 4
# x**3 + x**2 + x + 1

# Sample Output
# True

x, k = map(int, input().split())
print( k == (eval(input())) )