import sys, importlib

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QInputDialog
from PyQt5.QtTest import QTest
from design import AppUi
from scripts import AppScripts

class App(QMainWindow, AppUi, AppScripts):
    def __init__(self):
        super().__init__()
        self.tf = False

        with open('style.css', 'r') as css:
            self.setStyleSheet(css.read())

        self.renderBody(self)
        self.renderStartPage(self)
        self.renderTicTacToeStartPage(self)
        self.tictactoe_start_page.hide()

        self.build_handlers()

    def build_handlers(self):
        self.exit.clicked.connect(lambda : QApplication.exit())
        self.games_list_tictactoe.clicked.connect(self.tictactoeOpen)
        self.ttt_back.clicked.connect(self.tictactoeBack)
        self.ttt_start.clicked.connect(self.tictactoeStart)

    #-------Tic-Tac-Toe-Functions-----------#
    def tictactoeOpen(self):
        self.start_page.hide()
        self.tictactoe_start_page.show()

    def tictactoeBack(self):
        self.start_page.show()
        self.tictactoe_start_page.hide()

    def tictactoeStart(self):
        check = lambda string: any(char.isalpha() for char in string) or int(string)<0

        if self.ttt_width_line.text() == '':
            self.ttt_width_line.setText('3')

        if self.ttt_height_line.text() == '':
            self.ttt_height_line.setText('3')

        if self.ttt_win_cnt_line.text() == '':
            self.ttt_win_cnt_line.setText('3')

        if self.ttt_game_speed_line.text() == '':
            self.ttt_game_speed_line.setText('100')

        if check(self.ttt_width_line.text()) or check(self.ttt_height_line.text()) or check(self.ttt_win_cnt_line.text()) or check(self.ttt_game_speed_line.text()):
            self.ttt_start.setDisabled(True)
            self.showError("Введены некорректные данные!")
            QTest.qWait(100)#ms
            self.ttt_start.setDisabled(False)
            return False

        if int(self.ttt_win_cnt_line.text()) > min(int(self.ttt_width_line.text()), int(self.ttt_height_line.text())):
            self.ttt_start.setDisabled(True)
            self.showError("Введены некорректные данные!")
            QTest.qWait(100)# ms
            self.ttt_start.setDisabled(False)
            return False

        self.tictactoe_start_page.hide()
        self.renderTicTacToeGamePage(self)
        self.tictactoeGameRestart()

        self.ttt_compare.clicked.connect(self.tictactoeCompare)
        self.ttt_game_back.clicked.connect(self.tictactoeGameBack)
        self.ttt_restart.clicked.connect(self.tictactoeGameRestart)
        self.ttt_add_algorithm.clicked.connect(self.tictactoeOpenFile)


    def tictactoeComparator(self, first_player, second_player, alg_num1, alg_num2):
        #print(' - tictactoeComparator run')
        first_algorithm_module = importlib.import_module(f'algorithms.{self.ttt_algorithms_array[alg_num1]}')
        second_algorithm_module = importlib.import_module(f'algorithms.{self.ttt_algorithms_array[alg_num2]}')
        while self.ttt_end_game_result == '':
            if self.ttt_current_player == first_player:
                self.ttt_game_matrix = first_algorithm_module.algorithm(self.ttt_game_matrix, self.ttt_height,
                                                                        self.ttt_width, first_player)
            else:
                self.ttt_game_matrix = second_algorithm_module.algorithm(self.ttt_game_matrix, self.ttt_height,
                                                                         self.ttt_width, second_player)

            self.tictactoeRefreshGameField(App)
            QTest.qWait(self.ttt_game_speed)#ms

        winner_name = self.ttt_rating_table[alg_num1][0] if self.ttt_current_player==first_player else self.ttt_rating_table[alg_num2][0]
        winner_num = alg_num1 if self.ttt_current_player==first_player else alg_num2
        if self.ttt_end_game_result != 'draw':
            self.ttt_rating_table[winner_num][1] += 3
            self.ttt_current_winner_label.setText(self._translate("App", f"Победитель - {winner_name}"f"({self.ttt_current_player.upper()})"))
        else:
            self.ttt_rating_table[alg_num1][1] += 1
            self.ttt_rating_table[alg_num2][1] += 1
            self.ttt_current_winner_label.setText(self._translate("App", "Ничья"))

    def tictactoeCompare(self):
        if len(self.ttt_algorithms_array) < 2:
            self.ttt_compare.setDisabled(True)
            self.showError("Недостаточно алгоритмов для сравнения!")
            QTest.qWait(150)#ms
            self.ttt_compare.setDisabled(False)
            return False

        self.tictactoeSetAlgorithmsList()

        self.ttt_compare.setDisabled(True)
        self.ttt_add_algorithm.setDisabled(True)
        self.ttt_game_back.setDisabled(True)
        self.ttt_restart.setDisabled(True)

        first_player, second_player = 'x', 'o'
        for alg_num1 in range(len(self.ttt_algorithms_array)):
            for alg_num2 in range(alg_num1, len(self.ttt_algorithms_array)):
                if alg_num1 == alg_num2:
                    continue

                for i in range(2):
                    self.ttt_current_winner_label.setText(f'{self.ttt_rating_table[alg_num1][0]}({first_player.upper()}) '
                                                          f'vs {self.ttt_rating_table[alg_num2][0]}({second_player.upper()})')

                    self.tictactoeComparator(first_player, second_player, alg_num1, alg_num2)
                    QTest.qWait(1000)#ms

                    first_player, second_player = second_player, first_player

                    self.ttt_game_matrix = [['-1'] * self.ttt_width for i in range(self.ttt_height)]
                    self.ttt_current_player = 'x'
                    self.ttt_move_number = 0
                    self.ttt_end_game_result = ''

                    self.tictactoeClearField()

        self.ttt_algorithm_list.setPlainText('')
        self.ttt_rating_table.sort(key=lambda x: x[1], reverse=True)
        if self.ttt_rating_table[0][1] == self.ttt_rating_table[1][1]:
            self.ttt_algorithm_list.appendPlainText('Ничья!')
        else:
            self.ttt_algorithm_list.appendPlainText(f'{self.ttt_rating_table[0][0]} - победитель!')
        for i in range(len(self.ttt_rating_table)):
            name, score = self.ttt_rating_table[i]
            self.ttt_algorithm_list.appendPlainText(f'{i + 1} место - {name}: {score} баллов')

        self.ttt_game_back.setDisabled(False)
        self.ttt_restart.setDisabled(False)


    def tictactoeGameBack(self):
        self.tictactoe_start_page.show()
        self.tictactoe_game_page.hide()

    def tictactoeGameRestart(self):
        self.ttt_game_matrix = [['-1'] * self.ttt_width for i in range(self.ttt_height)]
        self.ttt_current_player = 'x'
        self.ttt_move_number = 0
        self.ttt_end_game_result = ''

        self.tictactoeSetAlgorithmsList()

        for i in range(len(self.ttt_rating_table)):
            self.ttt_rating_table[i][1] = 0
        self.tictactoeClearField()
        self.ttt_compare.setDisabled(False)
        self.ttt_add_algorithm.setDisabled(False)
        self.ttt_game_back.setDisabled(False)
        self.ttt_restart.setDisabled(False)

    def tictactoeOpenFile(self):
        nickname_availability, confirm = True, False
        while nickname_availability:
            nickname, confirm = QInputDialog.getText(self, 'Ввод', 'Название алгоритма:',
                                                     text=f'Algorithm{len(self.ttt_algorithms_array)+1}')
            if not confirm:
                break

            nickname_availability = nickname in [item for item, _ in self.ttt_rating_table]
            if nickname_availability:
                self.showError('Название алгоритма занято!')

        if confirm:
            algorithm_file, _ = QFileDialog.getOpenFileName(self, "Open Algorithm", "~", "Algorithm File (*.py)")
            if algorithm_file != '':
                if not algorithm_file in sys.path:
                    sys.path.insert(0, algorithm_file)
                self.ttt_algorithm_list.appendPlainText(algorithm_file)
                file_name = QUrl.fromLocalFile(algorithm_file).fileName().split('.')[0]
                self.ttt_algorithms_array.append(file_name)
                self.ttt_rating_table.append([nickname, 0])
                self.tictactoeSetAlgorithmsList()
                #print(self.ttt_algorithms_array)

    # -------Tic-Tac-Toe-Functions-End----------#

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()