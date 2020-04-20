
class AppScripts(object):
    def __init__(self):
        super().__init__()
        self.ttt_width = 1
        self.ttt_height = 1
        self.ttt_win_cnt = 1
        self.ttt_move_number = 0
        self.ttt_current_player = 'x'
        self.ttt_game_matrix = [['-1']]
        self.ttt_end_game_result = ''
        self.ttt_algorithms_array = []
        self.ttt_rating_table = []
        self.ttt_source_rating_table = []
        self.ttt_game_speed = 100  # ms
        self.ttt_game_speed_dir = {
            'Очень медленно': 500,
            'Медленно': 250,
            'Нормально': 100,
            'Быстро': 40,
            'Очень быстро': 20
        }
        self.ttt_first_player  = 'x'
        self.ttt_second_player = 'o'
        self.ttt_iterator = 0
        self.ttt_alg_num1 = 0
        self.ttt_alg_num2 = 1

    def nextMove(self):
        #print(' - nextMove run')
        self.ttt_current_player = 'o' if self.ttt_current_player == 'x' else 'x'
        self.ttt_move_number += 1

#---------------------------------Tic-Tac-Toe-Checks--------------------------------------------------------#

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