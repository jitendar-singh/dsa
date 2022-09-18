class Searching:
    def __init__(self,arr, target):
        self.arr = arr
        self.target = target
    
    def BinarySearch(self):
        left, right = 0, len(self.arr)-1
        while(left <= right):
            mid = (left+right)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

arr = [1,2,3,4,5,6,7,8,9,11,12,20,34,45,55,66,76,84,91,100]
target = 1020
search = Searching(arr, target)
result = search.BinarySearch()

if result != -1:
    print(target," found at ", result," postion")
else:
    print(target," not found in ",arr)

        