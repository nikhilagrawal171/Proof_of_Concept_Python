#You are a theif wants to collect max cost from n houses in such a manner you can't theft from adjacent houses.

n = int(input('Number of houses '))
house = list(map(int,input('Enter cost of houses: ').split(' ')))
cost  = [-1]*n
cost[0] = house[0]
cost[1] = max(house[0],house[1])

for i in range(2,n):
    cost[i] = max(cost[i-1],cost[i-2]+house[i])

print('Maximum cost :',cost[n-1])
