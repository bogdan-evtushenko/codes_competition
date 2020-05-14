def algorithm(matrix, height, width, player, winCount):
	for i in range(height - 1, -1, -1):
		for j in range(width - 1, -1, -1):
			if matrix[i][j] == '-1':
				matrix[i][j] = player
				return matrix