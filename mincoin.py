#Given a value V, if we want to make change for V cents, 
# and we have infinite supply of each of C = { C1, C2, .. , Cm} valued coins,
#  what is the minimum number of coins to make the change?

#Input: coins[] = {9, 6, 5, 1}, V = 11
#Output: Minimum 2 coins required
#We can use 1 coin of 6 cents and 1 coin of 5 cents
import sys

coins = list(map(int,input('Enter Coins: ').split()))
coins.sort()
n = int(input())
l = len(coins)

t = [[n for x in range(n+1)] for y in range(l)]

for i in range(l):
    t[i][0] = 0

for i in range(l):
    for j in range(1,n+1):
        if j<coins[i]:
            t[i][j] = t[i-1][j]
        else:
            # print(t[i][j-coins[i]]+1)
            # print(t[i-1][j])
            t[i][j] = min(t[i-1][j], 1+t[i][j-coins[i]])
    # print(t)
# print(t)
print(t[l-1][n],'coins required')


