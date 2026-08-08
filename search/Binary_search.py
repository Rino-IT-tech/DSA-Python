list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
target = 20
start = 0
end = len(list) -1

while start <= end:
    mid = (start + end) // 2
    if list[mid] == target:
        print("number is found the index is : ",mid)
        break
    elif list[mid] < target:
        start = mid + 1
    elif list[mid] > target:
        end = mid - 1
