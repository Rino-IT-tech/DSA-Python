arr = [1,2,3,45,6,77,8]
found = False
target = 6
for i in range(len(arr)):
    if arr[i] == target:
        print("target element index: ",i)
        found = True
        break
if not found:
    print("elemnt is not found")
