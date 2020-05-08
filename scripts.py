import numpy
import math

class AppScripts(object):
    def __init__(self):
        super().__init__()
        #----Tic-Tac-Toe-State-----#
        self.ttt_width = 1
        self.ttt_height = 1
        self.ttt_win_cnt = 1
        self.ttt_rounds_number = 1
        self.ttt_rounds__number_iter = 0
        self.ttt_move_number = 0
        self.ttt_current_player = 'x'
        self.ttt_game_matrix = [['-1']]
        self.ttt_end_game_result = ''
        self.ttt_algorithms_array = []
        self.ttt_rating_table = []
        self.ttt_source_rating_table = []
        self.ttt_game_speed_dir = {
            'Очень медленно': 500,
            'Медленно': 250,
            'Нормально': 150,
            'Быстро': 80,
            'Очень быстро': 20
        }
        self.ttt_game_speed = self.ttt_game_speed_dir['Нормально']
        self.ttt_game_speed_backup = self.ttt_game_speed_dir['Нормально']
        self.ttt_first_player  = 'x'
        self.ttt_second_player = 'o'
        self.ttt_iterator = 0
        self.ttt_global_iterator = 1
        self.ttt_alg_num1 = 0
        self.ttt_alg_num2 = 1
        self.ttt_is_skip_battle = False
        self.ttt_is_skip_game = False
        self.ttt_is_fast_show_results = False
        self.ttt_details_array = []

        #----Battleship-State-----#
        self.battleship_current_matrix = [['-1'] * 10 for i in range(10)]
        self.battleship_game_matrix_p1 = [['-1'] * 10 for i in range(10)]
        self.battleship_game_matrix_p2 = [['-1'] * 10 for i in range(10)]
        self.battleship_attack_matrix_p1 = [['-1'] * 10 for i in range(10)]
        self.battleship_attack_matrix_p2 = [['-1'] * 10 for i in range(10)]
        self.battleship_nickname_p1 = ''
        self.battleship_nickname_p2 = ''
        self.battleship_current_page = 1
        self.battleship_current_move = 'p1'
        self.battleship_end_game_result = ''
        self.battleship_game_speed_dir = {
            'Очень медленно': 200,
            'Медленно': 160,
            'Нормально': 80,
            'Быстро': 20,
            'Очень быстро': 10
        }
        self.battleship_game_speed = self.battleship_game_speed_dir['Нормально']
        self.battleship_global_iterator = 0
        self.battleship_points_p1 = 0
        self.battleship_points_p2 = 0
        self.battleship_is_skip_game = False
        self.battleship_rounds = 1

#--------------------------------------Battleship---------------------------------------------------#

    def battleshipNextMove(self):
        self.battleship_current_move = 'p1' if self.battleship_current_move == 'p2' else 'p2'

    #---------------------------------Battleship-Checks--------------------------------------------#

    def battleshipCorrectCheck(self, matrix):
        height, width = len(matrix), len(matrix[0])

        four_count = 0
        three_count = 0
        two_count = 0
        one_count = 0
        for row in matrix:
            four_count += row.count('4')
            three_count += row.count('3')
            two_count += row.count('2')
            one_count += row.count('1')

        if math.ceil(four_count/4) != 1:
            return [False, 'Количество кораблей на 4 клетки должно быть 1!']

        if math.ceil(three_count/3) != 2:
            return [False, 'Количество кораблей на 3 клетки должно быть 2!']

        if math.ceil(two_count/2) != 3:
            return [False, 'Количество кораблей на 2 клетки должно быть 3!']

        if one_count != 4:
            return [False, 'Количество кораблей на 1 клетку должно быть 4!']

        for i in range(height):
            for j in range(width - 1):
                if matrix[i][j] != matrix[i][j+1] and matrix[i][j+1] != '-1' and matrix[i][j] != '-1':
                    return [False, 'Расстояние между кораблями должно быть не меньше единицы!']

        for j in range(width):
            for i in range(height - 1):
                if matrix[i][j] != matrix[i+1][j] and matrix[i+1][j] != '-1' and matrix[i][j] != '-1':
                    return [False, 'Расстояние между кораблями должно быть не меньше единицы!']

        matrix = numpy.array(matrix)
        diagonals = [matrix[::-1, :].diagonal(i) for i in range(-1 * (width - 1), width)]
        diagonals.extend(matrix.diagonal(i) for i in range((width - 1), -1 * width, -1))
        diagonals = [item.tolist() for item in diagonals]
        for diagonal in diagonals:
            for i in range(len(diagonal) - 1):
                if diagonal[i] != diagonal[i+1] and diagonal[i+1] != '-1' and diagonal[i] != '-1':
                    return [False, 'Расстояние между кораблями должно быть не меньше единицы!']

        return [True, '']

    def battleshipGetHitCount(self, matrix):
        hit_count = 0
        for row in matrix:
            hit_count += row.count('+')
        return hit_count

#--------------------------------------Tic-Tac-Toe---------------------------------------------------#
    def nextMove(self):
        #print(' - nextMove run')
        self.ttt_current_player = 'o' if self.ttt_current_player == 'x' else 'x'
        self.ttt_move_number += 1

    #---------------------------------Tic-Tac-Toe-Checks--------------------------------------------#

    def getMax(self, tlp):
        #print(' - getMax run')
        cnt, path, max_cnt, max_path = 0, '', 0, ''
        tlp.append(('', ''))
        for i in range(len(tlp) - 1):
            if tlp[i][0] == tlp[i + 1][0] and tlp[i][0] != '-1':
                path += tlp[i][1] + ','
                cnt += 1
            else:
                if cnt > max_cnt:
                    cnt += 1
                    path += tlp[i][1] + ','
                    max_cnt, max_path = cnt, path
                cnt, path = 0, ''
        return [max_cnt, max_path]

    # --------------Horizontal-----------------#
    def ttt_check_horizontal(self):
        #print(' - ttt_check_horizontal run')
        for i in range(self.ttt_height):
            arr = [(self.ttt_game_matrix[i][j], (str(i) + '_' + str(j))) for j in range(self.ttt_width)]
            if len(arr)-[i[0] for i in arr].count('-1') >= self.ttt_win_cnt:
                max_res = self.getMax(arr)
                if max_res[0] >= self.ttt_win_cnt:
                    return [True, max_res[1][:-1]]
        return [False, 0]

    # --------------Vertical-----------------#
    def ttt_check_vertical(self):
        #print(' - ttt_check_vertical run')
        for i in range(self.ttt_width):
            arr = [(self.ttt_game_matrix[j][i], (str(j) + '_' + str(i))) for j in range(self.ttt_height)]
            if len(arr)-[i[0] for i in arr].count('-1') >= self.ttt_win_cnt:
                max_res = self.getMax(arr)
                if max_res[0] >= self.ttt_win_cnt:
                    return [True, max_res[1][:-1]]
        return [False, 0]

    # --------------Main-Diag-----------------#
    def ttt_check_main_diag(self):
        #print(' - ttt_check_main_diag run')

        if self.ttt_height < self.ttt_width:
            for j in range(self.ttt_height):
                arr = [(self.ttt_game_matrix[i][i - j],
                        str(i) + '_' + str(i - j)) for i in range(j, self.ttt_height)]
                if len(arr) - [i[0] for i in arr].count('-1') >= self.ttt_win_cnt:
                    max_res = self.getMax(arr)
                    if max_res[0] >= self.ttt_win_cnt:
                        return [True, max_res[1][:-1]]

            for l in range(abs(self.ttt_height - self.ttt_width) + 1):
                arr = [(self.ttt_game_matrix[i][l + i],
                        str(i) + '_' + str(l + i)) for i in range(self.ttt_height)]
                if len(arr) - [i[0] for i in arr].count('-1') >= self.ttt_win_cnt:
                    max_res = self.getMax(arr)
                    if max_res[0] >= self.ttt_win_cnt:
                        return [True, max_res[1][:-1]]

            for j in range(self.ttt_height):
                arr = [(self.ttt_game_matrix[i - j][abs(self.ttt_width - self.ttt_height) + i],
                        str(i - j) + '_' + str(abs(self.ttt_width - self.ttt_height) + i)) for i in
                       range(j, self.ttt_height)]
                if len(arr) - [i[0] for i in arr].count('-1') >= self.ttt_win_cnt:
                    max_res = self.getMax(arr)
                    if max_res[0] >= self.ttt_win_cnt:
                        return [True, max_res[1][:-1]]


        else:

            for j in range(self.ttt_width):
                arr = [(self.ttt_game_matrix[i - j][i],
                        str(i - j) + '_' + str(i)) for i in range(j, self.ttt_width)]
                if len(arr) - [i[0] for i in arr].count('-1') >= self.ttt_win_cnt:
                    max_res = self.getMax(arr)
                    if max_res[0] >= self.ttt_win_cnt:
                        return [True, max_res[1][:-1]]

            for l in range(abs(self.ttt_height - self.ttt_width) + 1):
                arr = [(self.ttt_game_matrix[l + i][i],
                        str(l + i) + '_' + str(i)) for i in range(self.ttt_width)]
                if len(arr) - [i[0] for i in arr].count('-1') >= self.ttt_win_cnt:
                    max_res = self.getMax(arr)
                    if max_res[0] >= self.ttt_win_cnt:
                        return [True, max_res[1][:-1]]

            for j in range(self.ttt_width):
                arr = [(self.ttt_game_matrix[self.ttt_height - self.ttt_width + i][i - j],
                        str(self.ttt_height - self.ttt_width + i) + '_' + str(i - j)) for i in range(j, self.ttt_width)]
                if len(arr) - [i[0] for i in arr].count('-1') >= self.ttt_win_cnt:
                    max_res = self.getMax(arr)
                    if max_res[0] >= self.ttt_win_cnt:
                        return [True, max_res[1][:-1]]

        return [False, 0]

    #--------------Side-Diag-----------------#
    def ttt_check_side_diag(self):
        #print(' - ttt_check_side_diag run')
        if self.ttt_height < self.ttt_width:
            for j in range(self.ttt_height):
                arr = [(self.ttt_game_matrix[i][(self.ttt_width - 1) - i + j],
                        str(i) + '_' + str((self.ttt_width - 1) - i + j)) for i in range(j, self.ttt_height)]

                if len(arr) - [i[0] for i in arr].count('-1') >= self.ttt_win_cnt:
                    max_res = self.getMax(arr)
                    if max_res[0] >= self.ttt_win_cnt:
                        return [True, max_res[1]]

            for r in range(abs(self.ttt_height - self.ttt_width) + 1):
                arr = [(self.ttt_game_matrix[i][(self.ttt_width - 1) - i - r],
                        str(i) + '_' + str((self.ttt_width - 1) - i - r)) for i in range(self.ttt_height)]

                if len(arr) - [i[0] for i in arr].count('-1') >= self.ttt_win_cnt:
                    max_res = self.getMax(arr)
                    if max_res[0] >= self.ttt_win_cnt:
                        return [True, max_res[1]]

            for j in range(self.ttt_height):
                arr = [(self.ttt_game_matrix[i - j][(self.ttt_width - 1) - abs(self.ttt_height - self.ttt_width) - i],
                        str(i - j) + '_' + str((self.ttt_width - 1) - abs(self.ttt_height - self.ttt_width) - i)) for i
                       in range(j, self.ttt_height)]

                if len(arr) - [i[0] for i in arr].count('-1') >= self.ttt_win_cnt:
                    max_res = self.getMax(arr)
                    if max_res[0] >= self.ttt_win_cnt:
                        return [True, max_res[1]]

        else:
            for j in range(self.ttt_width):
                arr = [(self.ttt_game_matrix[i - j][(self.ttt_width - 1) - i],
                        str(i - j) + '_' + str((self.ttt_width - 1) - i)) for i in range(j, self.ttt_width)]

                if len(arr) - [i[0] for i in arr].count('-1') >= self.ttt_win_cnt:
                    max_res = self.getMax(arr)
                    if max_res[0] >= self.ttt_win_cnt:
                        return [True, max_res[1]]

            for r in range(abs(self.ttt_height - self.ttt_width) + 1):
                arr = [(self.ttt_game_matrix[i + r][(self.ttt_width - 1) - i],
                        str(i + r) + '_' + str((self.ttt_width - 1) - i)) for i in range(self.ttt_width)]

                if len(arr) - [i[0] for i in arr].count('-1') >= self.ttt_win_cnt:
                    max_res = self.getMax(arr)
                    if max_res[0] >= self.ttt_win_cnt:
                        return [True, max_res[1]]

            for j in range(self.ttt_width):
                arr = [(self.ttt_game_matrix[(self.ttt_height - self.ttt_width) + i][(self.ttt_width - 1) - i + j],
                        str((self.ttt_height - self.ttt_width) + i) + '_' + str((self.ttt_width - 1) - i + j)) for i in
                       range(j, self.ttt_width)]

                if len(arr) - [i[0] for i in arr].count('-1') >= self.ttt_win_cnt:
                    max_res = self.getMax(arr)
                    if max_res[0] >= self.ttt_win_cnt:
                        return [True, max_res[1]]

        return [False, 0]