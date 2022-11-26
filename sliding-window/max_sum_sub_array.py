def maxSum(arr,windowSize):
    arraySize = len(arr)
    if(arraySize <= windowSize):
        print('Invalid Operation')
        return -1
    
    windowSum = sum([arr[i] for i in range(windowSize)])
    print("windowsum: ",windowSum)
    max_sum = windowSum
    print("maxsum: ",max_sum)

    for i in range(arraySize - windowSize):
        windowSum = windowSum - arr[i]+arr[i+windowSize]
        print("INSIDE LOOP: windowsum: ",windowSum)
        max_sum = max(windowSum, max_sum)
        print("INSIDELOOP: maxsum: ",max_sum)

    return max_sum

arr = [80,-50,90,100]
k = 2
result = maxSum(arr, k)
print("INFO Maximum Window Sum: ",result)