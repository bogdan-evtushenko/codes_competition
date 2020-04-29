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
        self.ttt_start.setFocus()

    def tictactoeBack(self):
        self.start_page.show()
        self.tictactoe_start_page.hide()

    def tictactoeStart(self):
        digits_check = lambda string: len([item for item in string if item.isdigit()])!=len(string)
        zero_check =  lambda string: string=='0'
        one_check = lambda string: string=='1'
        def showIncorrectData(text):
            self.ttt_start.setDisabled(True)
            self.showError(text)
            QTest.qWait(100)#ms
            self.ttt_start.setDisabled(False)
            return False

        width = self.ttt_width_line.text()
        height = self.ttt_height_line.text()
        win_cnt = self.ttt_win_cnt_line.text()
        rounds_number = self.ttt_rounds_number_line.text()

        if width == '':
            self.ttt_width_line.setText('3')
            width = self.ttt_width_line.text()

        if height == '':
            self.ttt_height_line.setText('3')
            height = self.ttt_height_line.text()

        if win_cnt == '':
            self.ttt_win_cnt_line.setText('3')
            win_cnt = self.ttt_win_cnt_line.text()

        if rounds_number == '':
            self.ttt_rounds_number_line.setText('1')
            rounds_number = self.ttt_rounds_number_line.text()

        if digits_check(width):
            return showIncorrectData('Ширина должна быть целым положительным числом!')
        if zero_check(width):
            return showIncorrectData('Ширина не может равняться нулю!')
        if one_check(width):
            return showIncorrectData('Ширина не может равняться единице!')

        if digits_check(height):
            return showIncorrectData('Высота должна быть целым положительным числом!')
        if zero_check(height):
            return showIncorrectData('Высота не может равняться нулю!')
        if one_check(height):
            return showIncorrectData('Высота не может равняться единице!')

        if digits_check(win_cnt):
            return showIncorrectData('Количество подряд идущих для победы должно быть '
                                     'целым положительным числом!')
        if zero_check(win_cnt):
            return showIncorrectData('Количество подряд идущих для победы не может равняться нулю!')
        if one_check(win_cnt):
            return showIncorrectData('Количество подряд идущих для победы не может равняться единице!')

        if digits_check(rounds_number):
            return showIncorrectData('Количество раундов для одной пары алгоритмов должно быть '
                                     'целым положительным числом!')
        if zero_check(rounds_number):
            return showIncorrectData('Количество раундов для одной пары алгоритмов не может равняться нулю!')

        if int(win_cnt) > min(int(width), int(height)):
            return showIncorrectData('Количество подряд идущих для победы не может быть '
                                     'больше минимального размера поля!')

        self.tictactoe_start_page.hide()
        self.renderTicTacToeGamePage(self)

        self.ttt_start.setDisabled(True)

        self.ttt_compare.clicked.connect(self.tictactoeCompare)
        self.ttt_game_back.clicked.connect(self.tictactoeGameBack)
        self.ttt_restart.clicked.connect(self.tictactoeGameRestart)
        self.ttt_add_algorithm.clicked.connect(self.tictactoeOpenFile)
        self.ttt_delete_all_algorithms.clicked.connect(self.tictactoeDeleteAllAlgorithms)

        self.tictactoeGameRestart()
        self.tictactoeChangeGameSpeed(self.ttt_set_speed_normal)

        self.ttt_set_speed_normal.triggered.connect(lambda: self.tictactoeChangeGameSpeed(self.ttt_set_speed_normal))
        self.ttt_set_speed_slow.triggered.connect(lambda: self.tictactoeChangeGameSpeed(self.ttt_set_speed_slow))
        self.ttt_set_speed_very_slow.triggered.connect(lambda: self.tictactoeChangeGameSpeed(self.ttt_set_speed_very_slow))
        self.ttt_set_speed_fast.triggered.connect(lambda : self.tictactoeChangeGameSpeed(self.ttt_set_speed_fast))
        self.ttt_set_speed_very_fast.triggered.connect(lambda: self.tictactoeChangeGameSpeed(self.ttt_set_speed_very_fast))

    def tictactoeComparator(self, first_player, second_player, alg_num1, alg_num2):
        #print(' - tictactoeComparator run')
        first_algorithm_module = importlib.import_module(f'algorithms.{self.ttt_algorithms_array[alg_num1]}')
        second_algorithm_module = importlib.import_module(f'algorithms.{self.ttt_algorithms_array[alg_num2]}')
        while self.ttt_end_game_result == '':
            if self.ttt_current_player == first_player:
                self.ttt_game_matrix = first_algorithm_module.algorithm(self.ttt_game_matrix, self.ttt_height,
                                                                        self.ttt_width, first_player, self.ttt_win_cnt)
            else:
                self.ttt_game_matrix = second_algorithm_module.algorithm(self.ttt_game_matrix, self.ttt_height,
                                                                         self.ttt_width, second_player, self.ttt_win_cnt)

            self.tictactoeRefreshGameField(App)
            QTest.qWait(self.ttt_game_speed)#ms

        winner_name = self.ttt_rating_table[alg_num1][0] if self.ttt_current_player==first_player else self.ttt_rating_table[alg_num2][0]
        winner_num = alg_num1 if self.ttt_current_player==first_player else alg_num2
        if self.ttt_end_game_result != 'draw':
            self.ttt_rating_table[winner_num][1] += 3

            if not self.ttt_is_fast_show_results:
                self.ttt_current_winner_label.setText(self._translate("App",
                    f"Победитель - {winner_name}({self.ttt_current_player.upper()})")
                )

            self.ttt_details_array.append(
                f'{self.ttt_rating_table[alg_num1][0]}({first_player.upper()}) '
                f'vs {self.ttt_rating_table[alg_num2][0]}({second_player.upper()})\n'
                f'  Победитель - {winner_name}({self.ttt_current_player.upper()})'
            )

        else:
            self.ttt_rating_table[alg_num1][1] += 1
            self.ttt_rating_table[alg_num2][1] += 1

            if not self.ttt_is_fast_show_results:
                self.ttt_current_winner_label.setText(self._translate("App", "Ничья"))

            self.ttt_details_array.append(
                f'{self.ttt_rating_table[alg_num1][0]}({first_player.upper()}) '
                f'vs {self.ttt_rating_table[alg_num2][0]}({second_player.upper()})\n'
                f'  Ничья'
            )

    def tictactoeCompare(self):
        if len(self.ttt_algorithms_array) < 2:
            self.ttt_compare.setDisabled(True)
            self.showError("Недостаточно алгоритмов для сравнения!")
            QTest.qWait(100)#ms
            self.ttt_compare.setDisabled(False)
            return False

        if self.ttt_step_by_step_mode.isChecked():
            self.tictactoeStepByStepCompareStart()
            return False

        self.tictactoeSetAlgorithmsList()

        self.ttt_compare.setDisabled(True)
        self.ttt_game_back.setDisabled(True)
        self.ttt_restart.setDisabled(True)
        self.ttt_delete_all_algorithms.setDisabled(True)
        self.ttt_step_by_step_mode.setDisabled(True)

        self.ttt_add_algorithm.setText(self._translate("App", "Завершить турнир"))
        self.ttt_add_algorithm.clicked.disconnect()
        self.ttt_add_algorithm.clicked.connect(self.tictactoeSkipGame)

        first_player, second_player = 'x', 'o'
        for alg_num1 in range(len(self.ttt_algorithms_array)):
            for alg_num2 in range(alg_num1, len(self.ttt_algorithms_array)):
                if alg_num1 == alg_num2:
                    continue

                for i in range(2):
                    for j in range(self.ttt_rounds_number):
                        if not self.ttt_is_fast_show_results:
                            self.ttt_current_winner_label.setText(self._translate("App",
                                f'{self.ttt_rating_table[alg_num1][0]}({first_player.upper()}) '
                                f'vs {self.ttt_rating_table[alg_num2][0]}({second_player.upper()})'
                            ))

                        self.tictactoeComparator(first_player, second_player, alg_num1, alg_num2)
                        QTest.qWait(self.ttt_game_speed*4)#ms

                        self.tictactoeSetDefaultValues()
                        self.tictactoeClearField()

                    first_player, second_player = second_player, first_player

                    self.tictactoeSetDefaultValues()
                    self.tictactoeClearField()

        self.tictactoeGetWinners()

        self.ttt_compare.setDisabled(False)
        self.ttt_compare.setText(self._translate("App", "Показать подробности"))
        self.ttt_compare.clicked.disconnect()
        self.ttt_compare.clicked.connect(self.tictactoeShowDetails)

        self.ttt_add_algorithm.setText(self._translate("App", "Добавить Алгоритм"))
        self.ttt_add_algorithm.setDisabled(True)
        self.ttt_add_algorithm.clicked.disconnect()
        self.ttt_add_algorithm.clicked.connect(self.tictactoeOpenFile)
        self.ttt_game_back.setDisabled(False)
        self.ttt_restart.setDisabled(False)
        self.ttt_delete_all_algorithms.setDisabled(False)

    def tictactoeSkipGame(self):
        self.ttt_game_speed = 0
        self.ttt_is_fast_show_results = True
        self.ttt_add_algorithm.setText(self._translate("App", "Добавить Алгоритм"))
        self.ttt_add_algorithm.setDisabled(True)
        self.ttt_add_algorithm.clicked.disconnect()
        self.ttt_add_algorithm.clicked.connect(self.tictactoeOpenFile)

    def tictactoeStepByStepFirstStep(self):
        #print(' - tictactoeStepByStepFirstStep run')
        self.ttt_compare.setText(self._translate("App", "Следующий шаг"))

        self.ttt_compare.clicked.disconnect()
        self.ttt_compare.clicked.connect(self.tictactoeStepByStepCompare)
        self.tictactoeStepByStepCompare()

    def tictactoeStepByStepComparator(self, first_player, second_player, alg_num1, alg_num2):
        #print(' - tictactoeStepByStepComparator run')
        if self.ttt_end_game_result == '':
            first_algorithm_module = importlib.import_module(f'algorithms.{self.ttt_algorithms_array[alg_num1]}')
            second_algorithm_module = importlib.import_module(f'algorithms.{self.ttt_algorithms_array[alg_num2]}')
            if self.ttt_current_player == first_player:
                self.ttt_game_matrix = first_algorithm_module.algorithm(self.ttt_game_matrix, self.ttt_height,
                                                                        self.ttt_width, first_player, self.ttt_win_cnt)
            else:
                self.ttt_game_matrix = second_algorithm_module.algorithm(self.ttt_game_matrix, self.ttt_height,
                                                                         self.ttt_width, second_player, self.ttt_win_cnt)
            self.tictactoeRefreshGameField(App)

        else:
            winner_name = self.ttt_rating_table[alg_num1][0] if self.ttt_current_player == first_player else self.ttt_rating_table[alg_num2][0]
            winner_num = alg_num1 if self.ttt_current_player == first_player else alg_num2
            if self.ttt_end_game_result != 'draw':
                self.ttt_rating_table[winner_num][1] += 3

                if not self.ttt_is_fast_show_results:
                    self.ttt_current_winner_label.setText(
                        self._translate("App", f"Победитель - {winner_name}({self.ttt_current_player.upper()})")
                    )

                self.ttt_details_array.append(
                    f'{self.ttt_rating_table[self.ttt_alg_num1][0]}({self.ttt_first_player.upper()}) '
                    f'vs {self.ttt_rating_table[self.ttt_alg_num2][0]}({self.ttt_second_player.upper()})\n'
                    f'  Победитель - {winner_name}({self.ttt_current_player.upper()})'
                )

            else:
                self.ttt_rating_table[alg_num1][1] += 1
                self.ttt_rating_table[alg_num2][1] += 1

                if not self.ttt_is_fast_show_results:
                    self.ttt_current_winner_label.setText(self._translate("App", "Ничья"))

                self.ttt_details_array.append(
                    f'{self.ttt_rating_table[self.ttt_alg_num1][0]}({self.ttt_first_player.upper()}) '
                    f'vs {self.ttt_rating_table[self.ttt_alg_num2][0]}({self.ttt_second_player.upper()})\n'
                    f'  Ничья'
                )

            if self.ttt_global_iterator != (len(self.ttt_algorithms_array) * (len(self.ttt_algorithms_array) - 1)) * self.ttt_rounds_number:
                self.ttt_compare.setText(self._translate("App", "Следующая битва"))
            else:
                self.ttt_compare.setText(self._translate("App", "Показать результаты"))

            if self.ttt_is_skip_game:
                QTest.qWait(self.ttt_game_speed*4)


    def tictactoeStepByStepCompare(self):
        #print(' - tictactoeStepByStepCompare run')
        if self.ttt_compare.text() == 'Следующая битва':
            self.tictactoeClearField()

            self.ttt_compare.clicked.disconnect()
            self.ttt_compare.clicked.connect(self.tictactoeStepByStepFirstStep)
            self.ttt_compare.setText(self._translate("App", "Первый шаг"))

            if not self.ttt_is_skip_game:
                self.ttt_skip_battle.setDisabled(False)

            self.ttt_rounds__number_iter += 1

            return False

        if self.ttt_end_game_result != '':
            self.tictactoeSetDefaultValues()
            self.tictactoeClearField()
            self.ttt_global_iterator += 1

            if self.ttt_rounds__number_iter == self.ttt_rounds_number or self.ttt_compare.text() == 'Показать результаты':
                self.ttt_rounds__number_iter = 0
                self.ttt_first_player, self.ttt_second_player = self.ttt_second_player, self.ttt_first_player
                self.ttt_iterator += 1
                if self.ttt_iterator == 2:
                    self.ttt_alg_num2 += 1
                    self.ttt_iterator = 0
                    if self.ttt_alg_num2 == len(self.ttt_algorithms_array):
                        self.ttt_alg_num1 += 1
                        self.ttt_alg_num2 = self.ttt_alg_num1 + 1
                        if self.ttt_alg_num2 == len(self.ttt_algorithms_array):
                            self.ttt_compare.setText(self._translate("App", "Сравнить алгоритмы"))

                            self.ttt_skip_battle.hide()
                            self.ttt_skip_game.hide()
                            self.ttt_add_algorithm.show()

                            self.ttt_game_back.setDisabled(False)
                            self.ttt_restart.setDisabled(False)
                            self.ttt_delete_all_algorithms.setDisabled(False)
                            self.ttt_step_by_step_mode.setDisabled(False)

                            self.ttt_compare.setDisabled(False)
                            self.ttt_compare.setText(self._translate("App", "Показать подробности"))
                            self.ttt_compare.clicked.disconnect()
                            self.ttt_compare.clicked.connect(self.tictactoeShowDetails)

                            self.tictactoeGetWinners()
                            return False

        #print(f'{self.ttt_alg_num1+1}vs{self.ttt_alg_num2+1}')

        if not self.ttt_is_fast_show_results:
            self.ttt_current_winner_label.setText(
                f'{self.ttt_rating_table[self.ttt_alg_num1][0]}({self.ttt_first_player.upper()}) '
                f'vs {self.ttt_rating_table[self.ttt_alg_num2][0]}({self.ttt_second_player.upper()})')

        self.tictactoeStepByStepComparator(self.ttt_first_player, self.ttt_second_player, self.ttt_alg_num1, self.ttt_alg_num2)
        if self.ttt_end_game_result != '':
            self.tictactoeStepByStepComparator(self.ttt_first_player, self.ttt_second_player, self.ttt_alg_num1, self.ttt_alg_num2)

    def tictactoeStepByStepCompareStart(self):
        self.ttt_compare.clicked.disconnect()
        self.ttt_compare.clicked.connect(self.tictactoeStepByStepFirstStep)
        self.ttt_compare.setText(self._translate("App", "Первый шаг"))

        self.ttt_add_algorithm.hide()
        self.ttt_skip_game.show()
        self.ttt_skip_battle.show()
        self.ttt_skip_game.clicked.connect(self.tictactoeStepByStepSkipGame)
        self.ttt_skip_battle.clicked.connect(self.tictactoeStepByStepSkipBattle)

        self.ttt_add_algorithm.setDisabled(True)
        self.ttt_game_back.setDisabled(True)
        self.ttt_restart.setDisabled(True)
        self.ttt_delete_all_algorithms.setDisabled(True)
        self.ttt_step_by_step_mode.setDisabled(True)
        self.ttt_skip_game.setDisabled(False)
        self.ttt_skip_battle.setDisabled(False)

        self.ttt_first_player = 'x'
        self.ttt_second_player = 'o'
        self.ttt_iterator = 0
        self.ttt_global_iterator = 1
        self.ttt_alg_num1 = 0
        self.ttt_alg_num2 = 1
        self.ttt_is_skip_battle = False
        self.ttt_is_skip_game = False

    def tictactoeStepByStepSkipBattle(self):
        self.ttt_is_skip_battle = True
        self.ttt_compare.hide()
        self.ttt_compare_disabled.show()
        self.ttt_skip_battle.setDisabled(True)
        self.ttt_skip_game.setDisabled(True)

        if self.ttt_compare.text() == 'Первый шаг':
            self.ttt_compare.click()
            QTest.qWait(self.ttt_game_speed)

        while self.ttt_end_game_result == '':
            self.ttt_compare.click()
            QTest.qWait(self.ttt_game_speed)

        self.ttt_skip_game.setDisabled(False)
        self.ttt_compare_disabled.hide()
        self.ttt_compare.show()
        self.ttt_is_skip_battle = False

    def tictactoeStepByStepSkipGame(self):
        self.ttt_is_skip_game = True
        self.ttt_compare.setDisabled(True)
        self.ttt_skip_battle.setDisabled(True)
        self.ttt_skip_game.setText(self._translate("App", "Показать результаты"))
        self.ttt_skip_game.clicked.disconnect()
        self.ttt_skip_game.clicked.connect(self.tictactoeSetZeroSpeed)

        while self.ttt_alg_num2 != len(self.ttt_algorithms_array):
            self.tictactoeStepByStepCompare()
            QTest.qWait(self.ttt_game_speed)

        self.ttt_skip_game.setText(self._translate("App", "Завершить турнир"))
        self.ttt_skip_game.clicked.disconnect()
        self.ttt_skip_game.clicked.connect(self.tictactoeStepByStepSkipGame)
        self.ttt_is_skip_game = False

    def tictactoeSetZeroSpeed(self):
        self.ttt_game_speed = 0
        self.ttt_is_fast_show_results = True

    def tictactoeGameBack(self):
        self.ttt_start.setDisabled(False)

        self.tictactoe_start_page.show()
        self.tictactoe_game_page.hide()

    def tictactoeGameRestart(self):
        self.tictactoeSetDefaultValues()
        if self.ttt_game_speed != self.ttt_game_speed_backup:
            self.ttt_game_speed = self.ttt_game_speed_backup

        self.ttt_rating_table = self.ttt_source_rating_table.copy()
        self.ttt_details_array = []
        self.ttt_is_fast_show_results = False

        self.tictactoeSetAlgorithmsList()

        for i in range(len(self.ttt_rating_table)):
            self.ttt_rating_table[i][1] = 0

        self.tictactoeClearField()

        self.ttt_compare.clicked.disconnect()
        self.ttt_compare.clicked.connect(self.tictactoeCompare)
        self.ttt_compare.setText(self._translate("App", "Сравнить алгоритмы"))
        self.ttt_compare.setDisabled(False)
        self.ttt_add_algorithm.setDisabled(False)
        self.ttt_game_back.setDisabled(False)
        self.ttt_restart.setDisabled(False)
        self.ttt_step_by_step_mode.setDisabled(False)

    def tictactoeOpenFile(self):
        nickname_availability, confirm, nickname = True, False, ''
        while nickname_availability:
            nickname, confirm = QInputDialog.getText(self, 'Ввод', 'Название алгоритма:',
                                                     text=f'Algorithm{len(self.ttt_algorithms_array)+1}')
            if not confirm:
                break

            if nickname in [item for item, _ in self.ttt_rating_table]:
                self.showError('Название алгоритма занято!')
                nickname_availability = True
            elif nickname == '':
                self.showError('Название алгоритма не может быть пустым!')
                nickname_availability = True
            else:
                nickname_availability = False

        if confirm:
            error, algorithm_file = True, ''

            while error:
                algorithm_file, _ = QFileDialog.getOpenFileName(self, "Open Algorithm", "~", "Algorithm File (*.py)")
                if algorithm_file != '':
                    with open(algorithm_file, 'r') as file:
                        if not 'def algorithm(matrix, height, width, player, winCount):' in file.read():
                            self.showError('Несоответствие формата файла-алгоритма!')
                        else:
                            error = False
                else:
                    error = False

            if algorithm_file != '':
                if not algorithm_file in sys.path:
                    sys.path.insert(0, algorithm_file)
                self.ttt_algorithm_list.appendPlainText(algorithm_file)
                file_name = QUrl.fromLocalFile(algorithm_file).fileName().split('.')[0]
                self.ttt_algorithms_array.append(file_name)
                self.ttt_rating_table.append([nickname, 0])
                self.ttt_source_rating_table.append([nickname, 0])
                self.tictactoeSetAlgorithmsList()
                self.ttt_delete_all_algorithms.setDisabled(False)
                #print(self.ttt_algorithms_array)

    def tictactoeChangeGameSpeed(self, speed_object):
        self.ttt_set_speed_very_fast.setDisabled(False), self.ttt_set_speed_fast.setDisabled(False),
        self.ttt_set_speed_very_slow.setDisabled(False), self.ttt_set_speed_slow.setDisabled(False),
        self.ttt_set_speed_normal.setDisabled(False)
        speed_object.setDisabled(True)
        self.ttt_game_speed = self.ttt_game_speed_dir[speed_object.text()]
        self.ttt_game_speed_backup = self.ttt_game_speed

    def tictactoeDeleteAllAlgorithms(self):
        if self.showConfirm('Вы уверены что хотите удалить все алгоритмы?'):
            self.ttt_algorithms_array.clear()
            self.ttt_source_rating_table.clear()
            self.tictactoeSetAlgorithmsList()
            self.tictactoeGameRestart()
            self.ttt_delete_all_algorithms.setDisabled(True)

    # -------Tic-Tac-Toe-Functions-End----------#

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()