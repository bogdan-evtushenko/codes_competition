def algorithm(matrix, height, width, player, winCount):
	for i in range(height):
		for j in range(width):
			if matrix[i][j] == '-1' and j % 2 == 0:
				matrix[i][j] = player
				return matrix

	for i in range(height):
		for j in range(width):
			if matrix[i][j] == '-1':
				matrix[i][j] = player
				return matrix
