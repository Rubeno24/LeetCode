def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix

# Example usage
arr = [2, 4, 6, 8]
prefix = prefix_sum(arr)
print(prefix)  # Output: [2, 6, 12, 20]

# Finding sum of subarray [1:3]
l, r = 1, 3
subarray_sum = prefix[r] - (prefix[l-1] if l > 0 else 0)
print(subarray_sum)  # Output: 18
