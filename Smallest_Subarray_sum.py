#Smallest Subarray with Sum ≥ S
#Problem:
#Find the minimum length of a contiguous subarray whose sum is ≥ S.
#Example:
#Array: 2 1 5 2 3 2, S = 7
#Output: 2 ([5,2])
# Smallest subarray with sum >= S (Variable Sliding Window)

arr = list(map(int, input("Enter elements: ").split()))
S = int(input("Enter target sum S: "))

window_sum = 0
left = 0
min_length = float('inf')

for right in range(len(arr)):
    window_sum += arr[right]

    while window_sum >= S:
        min_length = min(min_length, right - left + 1)
        window_sum -= arr[left]
        left += 1

if min_length == float('inf'):
    print("No such subarray")
else:
    print("Minimum length:", min_length)
