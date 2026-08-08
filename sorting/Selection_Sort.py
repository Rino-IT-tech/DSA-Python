arr = [3,2,5,4,1]

n = len(arr)

for i in range(n-1):
    min_element = i
    for j in range(i+1,n):
        if arr[j] < arr[min_element]:
            min_element = j
    arr[i],arr[min_element] = arr[min_element] , arr[i]
print(arr)
