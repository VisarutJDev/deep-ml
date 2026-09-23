def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	# n row
	# m column and position on vector
	n = 0
	m = 0
	retList = [0] * len(b)
	if len(a) != len(b):
		return -1
	while m < len(b) and n < len(a):
		retList[n] += a[n][m] * b[m]
		m += 1
		if m == len(b):
			n += 1
			m = 0
	return retList

	# a matrix 2 row
	# [ 1 2 ]
	# [ 2 4 ]
	# b vector
	# [ 1 2 ]
