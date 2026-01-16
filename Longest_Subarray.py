#Longest Subarray with At Most K Distinct Elements
#Problem:
#Find the length of the longest subarray with at most k distinct numbers.
#Example:
#Array: 1 2 1 2 3, k = 2
#/Output: 4 ([1,2,1,2])
# Longest subarray with at most k distinct elements

arr = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter k: "))

freq = {}
left = 0
max_length = 0

for right in range(len(arr)):
    freq[arr[right]] = freq.get(arr[right], 0) + 1

    while len(freq) > k:
        freq[arr[left]] -= 1
        if freq[arr[left]] == 0:
            del freq[arr[left]]
        left += 1

    max_length = max(max_length, right - left + 1)

print("Longest length:", max_length)
