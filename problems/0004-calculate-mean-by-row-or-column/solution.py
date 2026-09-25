def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	# define row and col idx with n row and m col
	# so when mode switch it just change idx to iterate
	# matrix[n][m] to calculate on row mode
	# matrix[m][n] to calculate on col mode
	n = 0
	m = 0
	means = []
	s = 0
	while n < len(matrix) and m < len(matrix[n]):
		if mode == "row":
			s += matrix[n][m]
			m += 1
			if m == len(matrix[n]):
				means.append(s/m)
				m = 0
				n += 1
				s = 0

		if mode == "column":
			s += matrix[n][m]
			n += 1
			if n == len(matrix):
				means.append(s/n)
				n = 0
				m += 1
				s = 0
			
	return means