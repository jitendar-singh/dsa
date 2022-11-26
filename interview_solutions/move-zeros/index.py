def moveZeros(arr):
    result = list()

    for i in arr:
        if i != 0:
            result.append(i)
    
    for i in range(int(len(arr)-len(result))):
        result.append(0)
    
    return result

arr = [0,1,0,3,5,1,0,0,0]
print(moveZeros(arr))