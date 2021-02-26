class AI:  # AI类
    def __init__(self):
        self.map = [[3 for x in range(23)] for y in range(23)]  # 棋盘（x:5-19）（y：5-19），0为空 1为玩家 2为电脑 3为边界
        self.empty_point = []  # 可落子点(x, y)

        # 棋型
        # 连四
        self.P_FOUR = [1, 1, 1, 1]
        self.C_FOUR = [2, 2, 2, 2]
        # 活三
        self.P_L_THREE_L = [0, 1, 1, 1]
        self.P_L_THREE_R = [1, 1, 1, 0]
        self.C_L_THREE_L = [0, 2, 2, 2]
        self.C_L_THREE_R = [2, 2, 2, 0]
        # 眠三1
        self.P_S_THREE_L_1 = [2, 1, 1, 1]
        self.P_S_THREE_L_W_1 = [3, 1, 1, 1]
        self.P_S_THREE_R_1 = [1, 1, 1, 2]
        self.P_S_THREE_R_W_1 = [1, 1, 1, 3]
        self.C_S_THREE_L_1 = [1, 2, 2, 2]
        self.C_S_THREE_L_W_1 = [3, 2, 2, 2]
        self.C_S_THREE_R_1 = [2, 2, 2, 1]
        self.C_S_THREE_R_W_1 = [2, 2, 2, 3]
        # 眠三2
        self.P_S_THREE_2 = [1, 1, 0, 1]
        self.C_S_THREE_2 = [2, 2, 0, 2]
        # 眠三3
        self.P_S_THREE_3 = [1, 0, 1, 1]
        self.C_S_THREE_3 = [2, 0, 2, 2]
        # 活二1
        self.P_L_TWO_1 = [0, 1, 1, 0]
        self.C_L_TWO_1 = [0, 2, 2, 0]
        # 活二2
        self.P_L_TWO_2 = [0, 1, 0, 1]
        self.C_L_TWO_2 = [0, 2, 0, 2]


    def findBestChess(self, data):  # AI入口
        self.reset()
        self.getMap(data)
        self.getEmptyPoint(data)
        score, move = self.score()
        print('最终落子：')
        print(score)
        print(move)
        return move

    def reset(self):  # 初始化
        self.map = [[3 for x in range(23)] for y in range(23)]
        self.empty_point.clear()

    def getMap(self, data):  # 获取游戏棋局
        for x in range(4, 19):
            for y in range(4, 19):
                self.map[x][y] = data[x-4][y-4]

    def getEmptyPoint(self, data):  # 获取可落子点
        for x in range(15):
            for y in range(15):
                if data[x][y] == 0:
                    self.empty_point.append((x, y))

    def score(self):  # 获取每个可落子点的分数并返回最高分和对应坐标
        score = [[(7-max(abs(x-7), abs(y-7))) for x in range(15)] for y in range(15)]  # 越靠近棋盘中心初始分越高
        dir = [(1, 0), (0, 1), (1, 1), (1, -1)]
        final_score = []

        # 具体得分
        for i in range(len(self.empty_point)):
            x, y = self.empty_point[i]
            x += 4
            y += 4
            for j in range(4):
                m, n = dir[j]
                type = [self.map[x-4*m][y-4*n], self.map[x-3*m][y-3*n], self.map[x-2*m][y-2*n], self.map[x-m][y-n],
                        self.map[x+m][y+n], self.map[x+2*m][y+2*n], self.map[x+3*m][y+3*n], self.map[x+4*m][y+4*n]]
                for k in range(5):
                    typecut = type[k:(k+4)]
                    if typecut == self.C_FOUR:
                        score[x-4][y-4] += 1000
                        print('电脑连四，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.P_FOUR:
                        score[x-4][y-4] += 500
                        print('玩家连四，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.P_L_THREE_L and k <= 3:
                        score[x-4][y-4] += 100
                        print('玩家活三L，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.P_L_THREE_R and k >= 4:
                        score[x-4][y-4] += 100
                        print('玩家活三R，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.C_L_THREE_L and k <= 3:
                        score[x-4][y-4] += 50
                        print('电脑活三L，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.C_L_THREE_R and k >= 4:
                        score[x-4][y-4] += 50
                        print('电脑活三R，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.P_S_THREE_L_1:
                        score[x-4][y-4] += 4
                        print('玩家眠三L1，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.P_S_THREE_L_W_1:
                        score[x-4][y-4] += 4
                        print('玩家眠三LW1，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.P_S_THREE_R_1:
                        score[x-4][y-4] += 4
                        print('玩家眠三R1，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.P_S_THREE_R_W_1:
                        score[x-4][y-4] += 4
                        print('玩家眠三RW1，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.P_S_THREE_2:
                        score[x-4][y-4] += 4
                        print('玩家眠三2，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.P_S_THREE_3:
                        score[x-4][y-4] += 4
                        print('玩家眠三3，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.C_S_THREE_L_1:
                        score[x-4][y-4] += 10
                        print('电脑眠三L1，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.C_S_THREE_L_W_1:
                        score[x-4][y-4] += 10
                        print('电脑眠三LW1，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.C_S_THREE_R_1:
                        score[x-4][y-4] += 10
                        print('电脑眠三R1，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.C_S_THREE_R_W_1:
                        score[x-4][y-4] += 10
                        print('电脑眠三RW1，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.C_S_THREE_2:
                        score[x-4][y-4] += 10
                        print('电脑眠三2，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.C_S_THREE_3:
                        score[x-4][y-4] += 10
                        print('电脑眠三3，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.P_L_TWO_1:
                        score[x-4][y-4] += 6
                        print('玩家活二1，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.P_L_TWO_2:
                        score[x-4][y-4] += 6
                        print('玩家活二2，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.C_L_TWO_1:
                        score[x-4][y-4] += 10
                        print('电脑活二1，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))
                    if typecut == self.C_L_TWO_2:
                        score[x-4][y-4] += 10
                        print('电脑活二2，坐标：%d, %d，方向：%d,起始点：%d' % (x-4, y-4, j, k))

        # 记录最终得分
        for j in range(len(self.empty_point)):
            x, y = self.empty_point[j]
            final_score.append((score[x][y], (x, y)))

        # 获取最高分
        final_score.sort(reverse=True)
        best_move = final_score[0]
        return best_move
