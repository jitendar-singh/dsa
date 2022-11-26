def maxSum(arr, window_length):
    arr_len = len(arr)
    if arr_len <= window_length:
        return -1
    
    window_sum = sum([arr[i] for i in range(window_length)])
    max_sum = window_sum

    for i in range(arr_len-window_length):
        window_sum = window_sum - arr[i] + arr[i+window_length]
        max_sum = max(window_sum, max_sum)
    
    return max_sum

a = [1, 2, 100, -1, 5]
answer = maxSum(a, 2)
print(answer)
