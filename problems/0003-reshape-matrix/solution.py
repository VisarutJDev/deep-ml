import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	# the way to detect Impossible Reshape is n*m < number of element
	# arr_1d.toList()
	if new_shape[0] * new_shape[1] < len(a) * len(a[0]): 
		return []
	
	return np.reshape(a, new_shape)