#There is a stair case of n steps you can climb either 1 stair or 2.Find all the possible ways to climb stair.
#Assume base stair as 1.
n = int(input('Enter number of steps'))
arr = [i for i in range(n)]
sol = [-1]*(n)
sol[0] = 1
sol[1] = 1
for i in range(2,n):
    sol[i] = sol[i-1]+sol[i-2]

print('Total number of possible ways:', sol[n-1])