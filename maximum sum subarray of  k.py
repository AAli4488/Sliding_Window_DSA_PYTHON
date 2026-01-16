Problem:
Given an array and integer k, find the maximum sum of any subarray of size k.
Example:
Array: 2 1 5 1 3 2, k = 3
Output: 9 (subarray [5,1,3])
# Maximum sum subarray of size k (Sliding Window)

arr = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter window size k: "))

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum = window_sum + arr[i] - arr[i - k]
    max_sum = max(max_sum, window_sum)

print("Maximum sum:", max_sum)
