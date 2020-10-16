#Find Max sum of consecutive subarray of an array.
arr = list(map(int,input('Enter Array: ').split(' ')))
amax = [-1]*len(arr)
amax[0] = arr[0]
for i in range(1,len(arr)):
    amax[i] = max(amax[i-1]+arr[i],arr[i])
print(amax)
print(max(amax))
