def max_subarray(array):
	cur_max = array[0]
	best_max = cur_max
	# If we want to keep track of what the subarray actually is
	start = 0
	end = 0

	for i in range(1, len(array)):
		# One liner
		#cur_max = max(array[i], cur_max + array[i])

		# If we want to keep track of what the subarray actually is
		if array[i] >= cur_max + array[i]:
			start = i
			cur_max = array[i]
		else:
			end = i
			cur_max = cur_max + array[i]

		best_max = max(cur_max, best_max)
		
	print('Subarray:', array[start:end+1])
	return best_max

if __name__ == '__main__':
	array = [-2, -3, 4, -1, -2, 1, 5, -3]
	print('Max Sum:', max_subarray(array))

