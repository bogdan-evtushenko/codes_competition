from PyQt5 import QtCore, QtGui, QtWidgets
from scripts import AppScripts

class AppUi(AppScripts):
    def __init__(self):
        super().__init__()
        self._translate = QtCore.QCoreApplication.translate


    #-----------------------------Start-Page---------------------------------------------------#

    def renderStartPage(self, App):
        #print(' - renderStartPage run')

        self.start_page = QtWidgets.QWidget(self.body)
        self.start_page.setObjectName("start_page")

        self.verticalLayout_StartPage = QtWidgets.QVBoxLayout(self.start_page)
        self.verticalLayout_StartPage.setContentsMargins(150, 0, 150, 0)
        self.verticalLayout_StartPage.setObjectName("verticalLayout_StartPage")

        self.project_name = QtWidgets.QLabel(self.start_page)
        self.project_name.setAlignment(QtCore.Qt.AlignCenter)
        self.project_name.setObjectName("project_name")
        self.verticalLayout_StartPage.addWidget(self.project_name)

        self.games_list = QtWidgets.QFormLayout()
        self.games_list.setObjectName("games_list")

        self.games_list_header = QtWidgets.QLabel(self.start_page)
        self.games_list_header.setAlignment(QtCore.Qt.AlignCenter)
        self.games_list_header.setObjectName("games_list_header")
        self.games_list.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.games_list_header)

        self.games_list_tictactoe = QtWidgets.QPushButton(self.start_page)
        self.games_list_tictactoe.setAutoDefault(True)
        self.games_list_tictactoe.setObjectName("games_list_tictactoe")
        self.games_list.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.games_list_tictactoe)

        self.games_list_other = QtWidgets.QPushButton(self.start_page)
        self.games_list_other.setEnabled(False)
        self.games_list_other.setObjectName("games_list_other")
        self.games_list.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.games_list_other)

        self.exit = QtWidgets.QPushButton(self.start_page)
        self.exit.setAutoDefault(True)
        self.exit.setObjectName("exit")
        self.games_list.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.exit)

        self.verticalLayout_StartPage.addLayout(self.games_list)
        self.verticalLayout_Body.addWidget(self.start_page)

        self.project_name.setText(self._translate("App", "Project 121"))
        self.games_list_tictactoe.setText(self._translate("App", "Крестики-Нолики"))
        self.games_list_other.setText(self._translate("App", "в разработке..."))
        self.games_list_header.setText(self._translate("App", "Игры"))
        self.exit.setText(self._translate("App", "Выйти"))

    #-----------------------------Start-Page-End-----------------------------------------------#


    #-----------------------------TicTacToe-Start-Page-----------------------------------------#

    def renderTicTacToeStartPage(self, App):
        #print(' - renderTicTacToeStartPage run')

        self.tictactoe_start_page = QtWidgets.QWidget(self.body)
        self.tictactoe_start_page.setObjectName("tictactoe_start_page")

        self.verticalLayout_TicTacToeStartPage = QtWidgets.QVBoxLayout(self.tictactoe_start_page)
        self.verticalLayout_TicTacToeStartPage.setObjectName("verticalLayout_TicTacToeStartPage")

        self.ttt_game_name = QtWidgets.QLabel(self.tictactoe_start_page)
        self.ttt_game_name.setAlignment(QtCore.Qt.AlignCenter)
        self.ttt_game_name.setObjectName("ttt_game_name")
        self.verticalLayout_TicTacToeStartPage.addWidget(self.ttt_game_name)

        self.ttt_inputs = QtWidgets.QGridLayout()
        self.ttt_inputs.setContentsMargins(100, -1, 100, -1)
        self.ttt_inputs.setObjectName("ttt_inputs")

        self.ttt_width_line = QtWidgets.QLineEdit(self.tictactoe_start_page)
        self.ttt_width_line.setAlignment(QtCore.Qt.AlignCenter)
        self.ttt_width_line.setObjectName("ttt_width_line")
        self.ttt_inputs.addWidget(self.ttt_width_line, 0, 0, 1, 1)

        self.ttt_height_line = QtWidgets.QLineEdit(self.tictactoe_start_page)
        self.ttt_height_line.setAlignment(QtCore.Qt.AlignCenter)
        self.ttt_height_line.setObjectName("ttt_height_line")
        self.ttt_inputs.addWidget(self.ttt_height_line, 0, 1, 1, 1)

        self.ttt_win_cnt_line = QtWidgets.QLineEdit(self.tictactoe_start_page)
        self.ttt_win_cnt_line.setAlignment(QtCore.Qt.AlignCenter)
        self.ttt_win_cnt_line.setObjectName("ttt_win_cnt_line")
        self.ttt_inputs.addWidget(self.ttt_win_cnt_line, 1, 0, 1, 2)

        self.ttt_rounds_number_line = QtWidgets.QLineEdit(self.tictactoe_start_page)
        self.ttt_rounds_number_line.setAlignment(QtCore.Qt.AlignCenter)
        self.ttt_rounds_number_line.setObjectName("ttt_win_cnt_line")
        self.ttt_inputs.addWidget(self.ttt_rounds_number_line, 2, 0, 1, 2)

        self.ttt_start = QtWidgets.QPushButton(self.tictactoe_start_page)
        self.ttt_start.setAutoDefault(True)
        self.ttt_start.setObjectName("ttt_start")
        self.ttt_start.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ttt_inputs.addWidget(self.ttt_start, 3, 0, 1, 2)

        self.verticalLayout_TicTacToeStartPage.addLayout(self.ttt_inputs)

        self.ttt_back = QtWidgets.QPushButton(self.tictactoe_start_page)
        self.ttt_back.setAutoDefault(True)
        self.ttt_back.setObjectName("ttt_back")
        self.verticalLayout_TicTacToeStartPage.addWidget(self.ttt_back)

        spacer = QtWidgets.QSpacerItem(40, 150, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_TicTacToeStartPage.addItem(spacer)

        self.verticalLayout_Body.addWidget(self.tictactoe_start_page)

        self.ttt_game_name.setText(self._translate("App", "Крестики-Нолики"))
        self.ttt_width_line.setPlaceholderText(self._translate("App", "Ширина (по умолчанию 3)"))
        self.ttt_height_line.setPlaceholderText(self._translate("App", "Высота (по умолчанию 3)"))
        self.ttt_win_cnt_line.setPlaceholderText(self._translate("App", "Количество подряд идущих для победы (по умолчанию 3)"))
        self.ttt_rounds_number_line.setPlaceholderText(self._translate("App", "Количество раундов для одной пары алгоритмов "
                                                                              "(по умолчанию 1)"))
        self.ttt_start.setText(self._translate("App", "Старт"))
        self.ttt_back.setText(self._translate("App", "Назад"))

    #-----------------------------TicTacToe-Start-Page-End-------------------------------------#

    #-----------------------------TicTacToe-Game-Page------------------------------------------#

    def renderTicTacToeGamePage(self, App):
        #print(' - renderTicTacToeGamePage run')

        self.ttt_width = int(self.ttt_width_line.text())
        self.ttt_height = int(self.ttt_height_line.text())
        self.ttt_win_cnt = int(self.ttt_win_cnt_line.text())
        self.ttt_rounds_number = int(self.ttt_rounds_number_line.text())

        self.ttt_game_matrix = [['-1'] * self.ttt_width for i in range(self.ttt_height)]

        self.tictactoe_game_page = QtWidgets.QWidget(self.body)
        self.tictactoe_game_page.setObjectName("tictactoe_game_page")

        self.verticalLayout_GamePage = QtWidgets.QVBoxLayout(self.tictactoe_game_page)
        self.verticalLayout_GamePage.setObjectName("verticalLayout_GamePage")

        self.tictactoe_game_field = QtWidgets.QGridLayout()
        self.tictactoe_game_field.setObjectName("tictactoe_game_field")
        self.tictactoe_game_field.setSpacing(0)
        self.tictactoe_game_field.setContentsMargins((220 - self.ttt_width*10), 0, (220 - self.ttt_width*10), 0)

        for i in range(self.ttt_height):
            for j in range(self.ttt_width):
                self.tictactoe_game_cell = QtWidgets.QPushButton(self.tictactoe_game_page)
                self.tictactoe_game_cell.setObjectName(f"tictactoe_game_cell_{i}_{j}")
                #self.tictactoe_game_cell.setText(f'{i}_{j}')
                self.tictactoe_game_cell_css = f"font-size: {460//(self.ttt_width+self.ttt_height)}px; color: #2A2A2A; background-color: transparent; border: 1px solid #2A2A2A;"
                self.tictactoe_game_cell.setStyleSheet(self.tictactoe_game_cell_css)
                size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
                size_policy.setHorizontalStretch(0)
                size_policy.setVerticalStretch(0)
                size_policy.setHeightForWidth(self.tictactoe_game_cell.sizePolicy().hasHeightForWidth())
                self.tictactoe_game_cell.setSizePolicy(size_policy)

                self.tictactoe_game_cell.setFocusPolicy(QtCore.Qt.NoFocus)

                self.tictactoe_game_cell.clicked.connect(self.tictactoeCellClick)

                self.tictactoe_game_field.addWidget(self.tictactoe_game_cell, i, j, 1, 1)

        self.verticalLayout_GamePage.addLayout(self.tictactoe_game_field)

        self.ttt_game_info = QtWidgets.QHBoxLayout()
        self.ttt_game_info.setObjectName("ttt_game_info")
        self.ttt_current_move_label = QtWidgets.QLabel(self.tictactoe_game_page)
        self.ttt_current_move_label.setMaximumHeight(50)
        self.ttt_current_move_label.setObjectName("ttt_current_move_label")
        self.ttt_game_info.addWidget(self.ttt_current_move_label)

        self.ttt_step_by_step_mode = QtWidgets.QCheckBox(self.tictactoe_game_page)
        self.ttt_step_by_step_mode.setObjectName("ttt_step_by_step_mode")
        self.ttt_step_by_step_mode.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ttt_game_info.addWidget(self.ttt_step_by_step_mode)

        self.ttt_current_winner_label = QtWidgets.QLabel(self.tictactoe_game_page)
        self.ttt_current_winner_label.setMaximumHeight(50)
        self.ttt_current_winner_label.setObjectName("ttt_current_winner_label")
        self.ttt_game_info.addWidget(self.ttt_current_winner_label)
        self.verticalLayout_GamePage.addLayout(self.ttt_game_info)

        self.tictactoe_edit_menu = QtWidgets.QGridLayout()
        self.tictactoe_edit_menu.setObjectName("tictactoe_edit_menu")

        self.ttt_add_algorithm = QtWidgets.QPushButton(self.tictactoe_game_page)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.ttt_add_algorithm.sizePolicy().hasHeightForWidth())
        self.ttt_add_algorithm.setSizePolicy(size_policy)
        self.ttt_add_algorithm.setObjectName("ttt_add_algorithm")
        self.tictactoe_edit_menu.addWidget(self.ttt_add_algorithm, 1, 2, 1, 1)
        self.ttt_add_algorithm.setAutoDefault(True)

        self.ttt_skip_buttons = QtWidgets.QVBoxLayout()
        self.ttt_skip_buttons.setObjectName("verticalLayout")

        self.ttt_skip_battle = QtWidgets.QPushButton(self.tictactoe_game_page)
        self.ttt_skip_battle.setObjectName("ttt_skip_battle")
        self.ttt_skip_battle.setAutoDefault(True)
        self.ttt_skip_buttons.addWidget(self.ttt_skip_battle)

        self.ttt_skip_game = QtWidgets.QPushButton(self.tictactoe_game_page)
        self.ttt_skip_game.setObjectName("ttt_skip_game")
        self.ttt_skip_game.setAutoDefault(True)
        self.ttt_skip_buttons.addWidget(self.ttt_skip_game)

        self.tictactoe_edit_menu.addLayout(self.ttt_skip_buttons, 1, 2, 1, 1)
        self.ttt_skip_battle.hide()
        self.ttt_skip_game.hide()

        self.ttt_compare = QtWidgets.QPushButton(self.tictactoe_game_page)
        self.ttt_compare.setObjectName("ttt_compare")
        self.ttt_compare.setAutoDefault(True)
        self.tictactoe_edit_menu.addWidget(self.ttt_compare, 1, 1, 1, 1)

        self.ttt_compare_disabled = QtWidgets.QPushButton(self.tictactoe_game_page)
        self.ttt_compare_disabled.setObjectName("ttt_compare")
        self.ttt_compare_disabled.setAutoDefault(True)
        self.tictactoe_edit_menu.addWidget(self.ttt_compare_disabled, 1, 1, 1, 1)
        self.ttt_compare_disabled.setDisabled(True)
        self.ttt_compare_disabled.hide()

        self.ttt_restart = QtWidgets.QPushButton(self.tictactoe_game_page)
        self.ttt_restart.setObjectName("ttt_restart")
        self.ttt_restart.setAutoDefault(True)
        self.tictactoe_edit_menu.addWidget(self.ttt_restart, 2, 1, 1, 1)

        self.ttt_game_back = QtWidgets.QPushButton(self.tictactoe_game_page)
        self.ttt_game_back.setObjectName("ttt_game_back")
        self.ttt_game_back.setAutoDefault(True)
        self.tictactoe_edit_menu.addWidget(self.ttt_game_back, 2, 2, 1, 1)

        self.ttt_algorithm_list = QtWidgets.QPlainTextEdit(self.tictactoe_game_page)
        self.ttt_algorithm_list.setMaximumHeight(110)
        self.ttt_algorithm_list.setReadOnly(True)
        self.ttt_algorithm_list.setObjectName("ttt_algorithm_list")
        self.ttt_algorithm_list.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ttt_algorithm_list.verticalScrollBar().setPageStep(1)
        self.ttt_algorithm_list.verticalScrollBar().setSingleStep(1)
        self.tictactoe_edit_menu.addWidget(self.ttt_algorithm_list, 1, 0, 1, 1)

        self.ttt_delete_all_algorithms = QtWidgets.QPushButton(self.tictactoe_game_page)
        self.ttt_delete_all_algorithms.setObjectName("ttt_delete_all_algorithms")
        self.ttt_delete_all_algorithms.setAutoDefault(True)
        self.tictactoe_edit_menu.addWidget(self.ttt_delete_all_algorithms, 2, 0, 1, 1)
        if len(self.ttt_algorithms_array)==0:
            self.ttt_delete_all_algorithms.setDisabled(True)

        self.verticalLayout_GamePage.addLayout(self.tictactoe_edit_menu)
        self.verticalLayout_Body.addWidget(self.tictactoe_game_page)

        self.ttt_menu_bar = QtWidgets.QMenuBar(App)
        self.ttt_menu_bar.setGeometry(QtCore.QRect(0, 0, 773, 21))
        self.ttt_menu_bar.setObjectName("ttt_menu_bar")

        self.ttt_speed_menu = QtWidgets.QMenu(self.ttt_menu_bar)
        self.ttt_speed_menu.setObjectName("ttt_speed_menu")

        App.setMenuBar(self.ttt_menu_bar)

        self.ttt_set_speed_very_slow = QtWidgets.QAction(App)
        self.ttt_set_speed_very_slow.setObjectName("ttt_set_speed_very_slow")

        self.ttt_set_speed_slow = QtWidgets.QAction(App)
        self.ttt_set_speed_slow.setObjectName("ttt_set_speed_slow")

        self.ttt_set_speed_normal = QtWidgets.QAction(App)
        self.ttt_set_speed_normal.setObjectName("ttt_set_speed_normal")

        self.ttt_set_speed_fast = QtWidgets.QAction(App)
        self.ttt_set_speed_fast.setObjectName("ttt_set_speed_fast")

        self.ttt_set_speed_very_fast = QtWidgets.QAction(App)
        self.ttt_set_speed_very_fast.setObjectName("ttt_set_speed_very_fast")

        self.ttt_speed_menu.addAction(self.ttt_set_speed_very_slow)
        self.ttt_speed_menu.addAction(self.ttt_set_speed_slow)
        self.ttt_speed_menu.addAction(self.ttt_set_speed_normal)
        self.ttt_speed_menu.addAction(self.ttt_set_speed_fast)
        self.ttt_speed_menu.addAction(self.ttt_set_speed_very_fast)

        self.ttt_menu_bar.addAction(self.ttt_speed_menu.menuAction())

        self.ttt_current_move_label.setText(self._translate("App", "Текущий ход: X"))
        self.ttt_step_by_step_mode.setText(self._translate("App", "Пошаговый режим"))
        self.ttt_current_winner_label.setText(self._translate("App", ""))
        self.ttt_add_algorithm.setText(self._translate("App", "Добавить Алгоритм"))
        self.ttt_skip_battle.setText(self._translate("App", "Завершить битву"))
        self.ttt_skip_game.setText(self._translate("App", "Завершить турнир"))
        self.ttt_compare.setText(self._translate("App", "Сравнить алгоритмы"))
        self.ttt_compare_disabled.setText(self._translate("App", "Следующий шаг"))
        self.ttt_game_back.setText(self._translate("App", "Назад"))
        self.ttt_restart.setText(self._translate("App", "Рестарт"))
        self.ttt_delete_all_algorithms.setText(self._translate("App", "Удалить все алгоритмы"))
        self.ttt_speed_menu.setTitle(self._translate("App", "Скорость"))
        self.ttt_set_speed_very_slow.setText(self._translate("App", "Очень медленно"))
        self.ttt_set_speed_slow.setText(self._translate("App", "Медленно"))
        self.ttt_set_speed_normal.setText(self._translate("App", "Нормально"))
        self.ttt_set_speed_fast.setText(self._translate("App", "Быстро"))
        self.ttt_set_speed_very_fast.setText(self._translate("App", "Очень быстро"))
        self.ttt_set_speed_very_slow.setText(self._translate("App", "Очень медленно"))
        self.ttt_set_speed_very_slow.setShortcut(self._translate("App", "Alt+1"))
        self.ttt_set_speed_slow.setText(self._translate("App", "Медленно"))
        self.ttt_set_speed_slow.setShortcut(self._translate("App", "Alt+2"))
        self.ttt_set_speed_normal.setText(self._translate("App", "Нормально"))
        self.ttt_set_speed_normal.setShortcut(self._translate("App", "Alt+3"))
        self.ttt_set_speed_fast.setText(self._translate("App", "Быстро"))
        self.ttt_set_speed_fast.setShortcut(self._translate("App", "Alt+4"))
        self.ttt_set_speed_very_fast.setText(self._translate("App", "Очень быстро"))
        self.ttt_set_speed_very_fast.setShortcut(self._translate("App", "Alt+5"))

    def tictactoeRefreshGameField(self, App):
        #print(' - refreshGameField run')
        if not self.ttt_is_fast_show_results:
            for i in range(self.ttt_height):
                for j in range(self.ttt_width):
                    if self.ttt_game_matrix[i][j] != '-1':
                        child = self.tictactoe_game_page.findChild(QtWidgets.QPushButton, f'tictactoe_game_cell_{i}_{j}')
                        child.setText(self._translate("App", f'{self.ttt_game_matrix[i][j]}'.upper()))

        if self.tictactoeCheckWin():
            #print(self.ttt_end_game_result)
            pass
        else:
            self.nextMove()
            self.tictactoeSetCurrentMoveLine()


    def tictactoeClearField(self):
        self.ttt_current_move_label.setText(f"Текущий ход: X")
        self.ttt_current_winner_label.setText(self._translate("App", ""))
        for i in range(self.ttt_height):
            for j in range(self.ttt_width):
                child = self.tictactoe_game_page.findChild(QtWidgets.QPushButton, f'tictactoe_game_cell_{i}_{j}')
                child.setText(self._translate("App", ''))
                child.setStyleSheet(self.tictactoe_game_cell_css)

    def tictactoeCellClick(self):
        cell = self.tictactoe_game_field.sender()
        x, y = int(cell.objectName().split('_')[-2]), int(cell.objectName().split('_')[-1])
        if self.ttt_game_matrix[x][y] != '-1':
            return False
        self.ttt_game_matrix[x][y] = self.ttt_current_player
        self.tictactoeRefreshGameField(self)
        if self.ttt_end_game_result == 'draw':
            self.ttt_current_winner_label.setText(self._translate("App", "Ничья"))
        #[print(*i) for i in self.ttt_game_matrix]

    def tictactoeSetCurrentMoveLine(self):
        self.ttt_current_move_label.setText(f"Текущий ход: {self.ttt_current_player.upper()}")

    def tictactoePathPaintCells(self, path):
        if self.ttt_is_fast_show_results:
            return False

        for item in path:
            if '_' in item:
                child = self.tictactoe_game_page.findChild(QtWidgets.QPushButton, f"tictactoe_game_cell_{item}")
                child.setStyleSheet(self.tictactoe_game_cell_css + 'background-color: #3EAC4A')
        return True

    def tictactoeCheckWin(self):
        if self.ttt_move_number == (self.ttt_width * self.ttt_height) - 1:
            #self.ttt_current_winner_label.setText(self._translate("App", "Ничья"))
            self.ttt_end_game_result = 'draw'
            return True

        horizontal_win = self.ttt_check_horizontal()
        if horizontal_win[0]:
            path = horizontal_win[1].split(',')
            self.tictactoePathPaintCells(path)
            #self.ttt_current_winner_label.setText(self._translate("App", f"Победитель - {self.ttt_current_player.upper()}"))
            self.ttt_game_matrix = [[self.ttt_current_player] * self.ttt_width for i in range(self.ttt_height)]
            self.ttt_end_game_result = self.ttt_current_player
            return True

        vertical_win = self.ttt_check_vertical()
        if vertical_win[0]:
            path = vertical_win[1].split(',')
            self.tictactoePathPaintCells(path)
            #self.ttt_current_winner_label.setText(self._translate("App", f"Победитель - {self.ttt_current_player.upper()}"))
            self.ttt_game_matrix = [[self.ttt_current_player] * self.ttt_width for i in range(self.ttt_height)]
            self.ttt_end_game_result = self.ttt_current_player
            return True

        main_diag_win = self.ttt_check_main_diag()
        if main_diag_win[0]:
            path = main_diag_win[1].split(',')
            self.tictactoePathPaintCells(path)
            #self.ttt_current_winner_label.setText(self._translate("App", f"Победитель - {self.ttt_current_player.upper()}"))
            self.ttt_game_matrix = [[self.ttt_current_player] * self.ttt_width for i in range(self.ttt_height)]
            self.ttt_end_game_result = self.ttt_current_player
            return True

        side_diag_win = self.ttt_check_side_diag()

        if side_diag_win[0]:
            path = side_diag_win[1].split(',')
            self.tictactoePathPaintCells(path)
            #self.ttt_current_winner_label.setText(self._translate("App", f"Победитель - {self.ttt_current_player.upper()}"))
            self.ttt_game_matrix = [[self.ttt_current_player] * self.ttt_width for i in range(self.ttt_height)]
            self.ttt_end_game_result = self.ttt_current_player
            return True
        return False

    def tictactoeSetAlgorithmsList(self):
        algorithms_list = ''
        for item, _ in self.ttt_rating_table:
            algorithms_list += f'\n - {item}'
        self.ttt_algorithm_list.setPlainText(f'Алгоритмы: {algorithms_list}')

    def tictactoeGetWinners(self):
        self.ttt_algorithm_list.setPlainText('')
        self.ttt_rating_table.sort(key=lambda x: x[1], reverse=True)
        if self.ttt_rating_table[0][1] == self.ttt_rating_table[1][1]:
            self.ttt_algorithm_list.appendPlainText('Ничья!')
        else:
            self.ttt_algorithm_list.appendPlainText(f'{self.ttt_rating_table[0][0]} - победитель!')

        self.ttt_rating_table.append(['', ''])
        iter_place = 1

        for i in range(len(self.ttt_rating_table) - 1):
            name, score = self.ttt_rating_table[i]
            count_winners = [score for _, score in self.ttt_rating_table].count(score)
            win_place = f'{iter_place}-{iter_place + count_winners - 1}' if count_winners > 1 else f'{iter_place}'
            self.ttt_algorithm_list.appendPlainText(f'{win_place} место - {name}: {score} баллов')
            if self.ttt_rating_table[i][1] != self.ttt_rating_table[i + 1][1]:
                iter_place += count_winners

        self.ttt_rating_table.pop()

        self.ttt_algorithm_list.verticalScrollBar().setValue(0)

        self.ttt_compare.clicked.disconnect()
        self.ttt_compare.clicked.connect(self.tictactoeShowDetails)
        self.ttt_compare.setText(self._translate("App", "Показать подробности"))

    def tictactoeSetDefaultValues(self):
        self.ttt_game_matrix = [['-1'] * self.ttt_width for i in range(self.ttt_height)]
        self.ttt_current_player = 'x'
        self.ttt_move_number = 0
        self.ttt_end_game_result = ''

    def tictactoeShowDetails(self):
        #print(' - tictactoeShowDetails run')
        self.ttt_algorithm_list.setPlainText('')

        for i, item in enumerate(self.ttt_details_array):
            self.ttt_algorithm_list.appendPlainText(f' {i+1}. {item}\n')

        self.ttt_compare.clicked.disconnect()
        self.ttt_compare.clicked.connect(self.tictactoeGetWinners)
        self.ttt_compare.setText(self._translate("App", "Показать результаты"))
        self.ttt_algorithm_list.verticalScrollBar().setValue(0)

    #-----------------------------TicTacToe-Game-Page-End--------------------------------------#

    #-----------------------------Body---------------------------------------------------------#
    def renderBody(self, App):
        #print(' - renderBody run')

        App.setObjectName("App")
        App.resize(1024, 768)
        App.setMinimumSize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        App.setFont(font)

        self.setWidgetIcons(App)

        self.body = QtWidgets.QWidget(App)
        self.body.setObjectName("body")
        self.verticalLayout_Body = QtWidgets.QVBoxLayout(self.body)
        self.verticalLayout_Body.setObjectName("verticalLayout_Body")

        App.setCentralWidget(self.body)

        QtCore.QMetaObject.connectSlotsByName(App)

        App.setWindowTitle(self._translate("App", "Project121"))

    def setWidgetIcons(self, Widget):
        app_icon = QtGui.QIcon()
        app_icon.addFile('img/16x16.png', QtCore.QSize(16, 16))
        app_icon.addFile('img/24x24.png', QtCore.QSize(24, 24))
        app_icon.addFile('img/32x32.png', QtCore.QSize(32, 32))
        app_icon.addFile('img/48x48.png', QtCore.QSize(48, 48))
        app_icon.addFile('img/256x256.png', QtCore.QSize(256, 256))
        Widget.setWindowIcon(app_icon)

    def showError(self, text):
        msg = QtWidgets.QMessageBox()
        self.setWidgetIcons(msg)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(f'{text}\t')
        msg.setWindowTitle("Error")
        msg.exec_()

    def showConfirm(self, text):
        msg = QtWidgets.QMessageBox()
        self.setWidgetIcons(msg)
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(f'{text}\t')
        msg.setWindowTitle('Warning')
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        return msg.exec_() == QtWidgets.QMessageBox.Yes

    #-----------------------------Body-End-----------------------------------------------------#