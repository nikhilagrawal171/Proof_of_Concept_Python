#Given a value N, if we want to make change for N cents,
#  and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, 
# how many ways can we make the change? The order of coins doesn’t matter


#No of ways
#For example, for N = 4 and S = {1,2,3},
#  there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}.
#  So output should be 4.
#  For N = 10 and S = {2, 5, 3, 6}, 
# there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}.
#  So the output should be 5.
s = list(map(int,input('Enter Coins: ').split()))
s.sort()
n = int(input(''))
l = len(s)
t = [[1 if x==0 else 0 for x in range(n+1)] for y in range(l)]

#for i in range(l):
#    t[i][0] = 1

for i in range(n+1):
    if i%s[0]==0:
        t[0][i] = 1

for i in range(1,l):
    for j in range(1,n+1):
        if j<s[i]:
            t[i][j] = t[i-1][j]
        else:
            t[i][j] = t[i-1][j]+t[i][j-s[i]]
print('No of ways: ',t[l-1][n])
