Average of All Subarrays of Size K
Problem:
Print the average of every subarray of size k.
Example:
Array: 1 3 2 6 -1 4 1 8 2, k = 5
# Average of all subarrays of size k

arr = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter window size k: "))

window_sum = sum(arr[:k])
print("Average:", window_sum / k)

for i in range(k, len(arr)):
    window_sum = window_sum + arr[i] - arr[i - k]
    print("Average:", window_sum / k)
