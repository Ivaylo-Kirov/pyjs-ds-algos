# Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
# A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers <span>[1, 3, 4]</span> form a subsequence of the array <span>[1, 2, 3, 4]</span>, and so do the numbers <span>[2, 4]</span>. Note that a single number in an array and the array itself are both valid subsequences of the array.

def isValidSubsequence(array, sequence):
    # Write your code here.
	cur_i = 0
	matched = 0
	# go through each seq number
	for i in range(len(sequence)):
		# look for num in array
		while cur_i < len(array):
			if array[cur_i] == sequence[i]:
				cur_i += 1
				matched += 1
				break
			cur_i += 1
		if cur_i >= len(array) and i + 1 < len(sequence):
			return False
	if matched < len(sequence):
		return False
	return True

result = isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -1])
print(result)