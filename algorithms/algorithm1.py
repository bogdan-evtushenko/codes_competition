def algorithm(matrix, height, width, player):
	for i in range(height):
		for j in range(width):
			if matrix[i][j] == '-1' and j % 2 == 0:
				matrix[i][j] = player
				return matrix
		if matrix[i][j] == '-1':
				matrix[i][j] = player
				return matrix