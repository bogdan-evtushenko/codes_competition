def func(mas, pole, kolPole):
	for i in range(kolPole):
		if mas[i] == 0:
			mas[i] = 1
			pole[i].invoke() #нажатие кнопки
			break

