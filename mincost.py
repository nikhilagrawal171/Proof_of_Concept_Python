#find min cost to travel from 0,0 to n,n in 2D array of nxn such that you can either move right or down.
r = int(input('Enter no of Rows: '))
c = int(input('Enter no of Columns: '))
arr = [[int(input()) for x in range (c)] for y in range(r)] 
print(arr)

sol = [[-1 for i in range(c)] for j in range(r)]
sol[0][0] = arr[0][0]

#Min cost to cross first row
for i in range(1,c):
    sol[0][i] = sol[0][i-1]+arr[0][i]


#Min cost to cross first column
for j in range(1,r):
    sol[j][0] = sol[j-1][0]+arr[j][0]

for i in range(0,r):
    for j in range(0,c):
        if(sol[i][j] != -1):
            sol[i][j] = min(sol[i-1][j],sol[i][j-1])

print(sol)
print(sol[r-1][c-1])