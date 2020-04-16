#!/usr/bin/python3
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import Menu
from tkinter import ttk
from functools import partial
import tkinter.scrolledtext as tkst
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import random
import time
import sys
import os

algo = open("first.py", "w")
algo.close()
#global first
#import first
algo1 = open("second.py", "w")
algo1.close()
#global second
#import second
def clear():
    list = root.grid_slaves()

    for l in list:
        l.destroy()

def restart_program(event):
    python = sys.executable
    os.execl(python, python, * sys.argv)

def tic_run(kolRow, kolColumn):
    clear()
    global vector
    global coordinate
    vector = []
    coordinate = ()

    if kolRow >= 5:
        toWin = 5 #сколько клеток нужно для победы
    else:
        toWin = max(kolRow, kolColumn)

    global kolPole
    kolPole = kolRow*kolColumn
    kolColumn -= 1
    kolRow -= 1
    global switch
    switch = ['X', 'O'] #чтобы ставить Х или О
    global move
    move = int(0) #определяет, чья очередь
    global win
    win = False #победа
    global pole
    pole = [i for i in range(kolPole)]
    global mas
    mas = [0 for i in range(kolPole)]

    def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)

    global firstAlgo_bool
    global secondAlgo_bool

    firstAlgo_bool = False
    secondAlgo_bool = False

    def Competitor():
        if(firstAlgo_bool and secondAlgo_bool):
            root.update()

            while not win:
                first.func(mas, pole, kolPole)
                time.sleep(0.4)
                second.func(mas, pole, kolPole)
                time.sleep(0.4)
        else:
            mb.showinfo('Error', 'Choose files for compare')

    def tic_tac_toe(n): #один ход
        root.update() #обновить окно
        #print(str(n))
        global move
        global win
        global vector
        global coordinate
        mas[n] = move + 1
        pole[n]['bg'] = "silver" #серебряный цвет
        pole[n]['text'] = switch[move] #рисует Х и О
        pole[n].config(state='disabled') #деактивирует клетку, куда поставили Х или О
        

        for i in range(len(vector)):
            for j in range(len(vector[0])):
                if vector[i][j] == n: #идем по вектору выигрышных кобинаций
                    vector[i][j] = switch[move] #находим n-ю клетку, заменяем ее значение на Х или О

        for index in range(len(vector)):
            if vector[index].count('X') == len(vector[0]) or vector[index].count('O') == len(vector[0]): #если Х или О
                                                            #уже 5 в выигрышной комбинации
                win = True #победа

                for k in coordinate[index]: #находим клетки в выигрышной позиции
                    #print(i) #какие номера клеток
                    pole[k]['bg'] = 'light blue' #меняем их цвет
                break

        if win:
            for i in range(kolPole):
                pole[i].config(state='disabled') #все деактивируем
            '''FirstAlgoText.config(state='disabled')
            SecondAlgoText.config(state='disabled')
            Compare.config(state='disabled')'''
                
        if move == 0: #переход хода
            move = 1
        else:
            move = 0

        #print(mas)
        flag = True
        counter = 0
        for i in mas: #проверка на ничью
            if i != 0 and not win:
                counter += 1
        #print(counter)
        if counter == kolPole:
            Draw()
            #return 0
        #return 0

    def createButtons():
        root.update()
        columns = kolColumn
        rows = -1
        for indexPole in range(kolPole): #создаем кнопки
                if columns != kolColumn:
                    columns += 1
                else:
                    columns = 0
                    rows += 1

                #print(str(indexPole))
                #print(str(rows))
                #print(str(columns))
                pole[indexPole] = Button(root, command = partial(tic_tac_toe, indexPole), width=4, height=2, font=15)
                pole[indexPole].grid(row = rows, column = columns)
    
    def createWinningContainers(): #создание контейнеров с выигрышными кнопками
        root.update()
        global vector
        global coordinate

        knopka = -1
        for i in range(kolRow+1): #создаем вектор выигрышных кнопок
            for j in range(kolColumn+1):
                tempVector = [] #по горизонтали
                knopka += 1
                if (j < kolColumn-3) or (kolRow < 5 and j == 0):
                    tempKnopka = knopka
                    for counter in range(toWin):
                        tempVector.append(tempKnopka)
                        tempKnopka += 1
                if tempVector:
                    vector.append(tempVector)

                tempVector = [] #по вертикали
                if (i < kolRow-3) or (kolColumn < 5 and i == 0):
                    tempKnopka = knopka
                    for counter in range(toWin):
                        tempVector.append(tempKnopka)
                        tempKnopka = tempKnopka + kolColumn + 1
                if tempVector:
                    vector.append(tempVector)

                tempVector = [] #по диагонали слева направо
                if (i < kolRow-3 and j < kolColumn) or (kolColumn < 5 and j == 0 and i == 0):
                    tempKnopka = knopka
                    for counter in range(toWin):
                        tempVector.append(tempKnopka)
                        tempKnopka += kolColumn + 2
                if tempVector:
                    vector.append(tempVector)

                tempVector = [] #по диагонали справа налево
                if (i < kolRow-3 and j > 3) or (kolColumn < 5 and j == kolColumn and i == 0):
                    tempKnopka = knopka
                    for counter in range(toWin):
                        tempVector.append(tempKnopka)
                        tempKnopka += kolColumn
                if tempVector:
                    vector.append(tempVector)

        tempVector = []
        for i in range(len(vector)):
            tempTuple = tuple(vector[i])
            tempVector.append(tempTuple)

        #создали кортеж (не изменный)
        coordinate = tuple(tempVector)

    def Start():
        createWinningContainers()
        createButtons()

    Start()

    def ask_name(event, num):
        file_name = fd.askopenfilename(filetypes = [("other","*.py")])
        
        if file_name:
            f = open(os.path.abspath(file_name), "r")
            
            text = f.read()

            if text != "":
                if num == 1:
                    algo2 = open("first.py", "w")

                    algo2.write(text)

                    algo2.close()

                    global first
                    import first

                    global firstAlgo_bool
                    firstAlgo_bool = True

                else:
                    algo3 = open("second.py", "w")

                    algo3.write(text)

                    algo3.close()
                    global second
                    import second

                    global secondAlgo_bool
                    secondAlgo_bool = True
            else:
                mb.showinfo('Error', 'Chosen file is empty')

            f.close()

        else:
            mb.showinfo('Info', 'You should choose a file')

        return

    firstAlgo = Button(root, text = "Add first algo") #кнопка для
    firstAlgo.grid(row = 0, column = kolColumn+2)

    firstAlgo.bind('<Button-1>', lambda event, f = 1: ask_name(event, f))
    firstAlgo.bind('<Return>', lambda event, f = 1: ask_name(event, f))

    secondAlgo = Button(root, text = "Add second algo") #кнопка для
    secondAlgo.grid(row = 0, column = kolColumn+4)

    secondAlgo.bind('<Button-1>', lambda event, f = 2: ask_name(event, f))
    secondAlgo.bind('<Return>', lambda event, f = 2: ask_name(event, f))

    Compare = Button(root, text = "Compare the algorithms", command = Competitor) #кнопка для
    Compare.grid(row = 1, column = kolColumn+2)

    RestartButton = Button(root, text = "Restart", command = partial(tic_run, kolRow + 1, kolColumn + 1)) #кнопка для рестарта
    RestartButton.grid(row = 2, column = kolColumn+2)

    """StartButton = Button(root, text = 'Start', command=Start)
    StartButton.grid(row = 2, column = kolColumn+2)"""

    BackButton = Button(root, text = "Back") #кнопка для
    BackButton.grid(row = 3, column = kolColumn+2)

    BackButton.bind('<Button-1>', tic_tac_toe_func)
    BackButton.bind('<Return>', tic_tac_toe_func)

    return

def tic_tac_toe_func(event):
    def next_func(event):
        if get_raw_enter.get() and get_column_enter.get():
            kolRow = int(get_raw_enter.get())
            kolColumn = int(get_column_enter.get())
            tic_run(kolRow, kolColumn)
            return
        else:
            mb.showinfo('Error', 'Incorrect values')
            return
    
        return

    global root
    clear()
    get_raw_lab = Label(text = "Кол-во строк:", font = ("Comic Sans MS", 20, "bold"))
    get_raw_lab.grid(row = 0)
    get_raw_enter = Entry()
    get_raw_enter.grid(row = 1)

    get_column_lab = Label(text = "Кол-во столбцов:", font = ("Comic Sans MS", 20, "bold"))
    get_column_lab.grid(row = 2)
    get_column_enter = Entry()
    get_column_enter.grid(row = 3)

    next_button = Button(text = "Next")
    next_button.grid(row = 4)

    back_button = Button(text = "Back")
    back_button.grid(row = 5)
    
    next_button.bind('<Button-1>', next_func)
    next_button.bind('<Return>', next_func)

    back_button.bind('<Button-1>', restart_program)
    back_button.bind('<Return>', restart_program)

    return

root = Tk()
root.minsize(800, 600) #размер окна
root.resizable(width = True, height = True)

clear()

games_label = Label(text = "Игры:", font = ("Comic Sans MS", 20, "bold"))
games_label.grid(row = 0)

tic_tac_toe_button = Button(root, text = "Tic Tac Toe")
tic_tac_toe_button.grid(row = 1)

tic_tac_toe_button.bind('<Button-1>', tic_tac_toe_func)
tic_tac_toe_button.bind('<Return>', tic_tac_toe_func)

exit_button = Button(root, text = "Exit")
exit_button.grid(row = 2)

def close(event):
    os.remove("first.py")
    os.remove("second.py")
    root.destroy()

exit_button.bind('<Button-1>', close)
exit_button.bind('<Return>', close)

root.protocol("WM_DELETE_WINDOW", partial(close, algo))

root.mainloop()
