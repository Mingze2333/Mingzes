class AI:
    def __init__(self):
        self.map = [[3 for x in range(23)] for y in range(23)]  # 棋盘（x:5-19）（y：5-19），0为空 1为玩家 2为电脑 3为边界
        self.empty_point = []  # 可落子点(x, y)
        self.pos_score = [[(7-max(abs(x-7), abs(y-7))) for x in range(15)] for y in range(15)]  # 越靠近棋盘中心初始分越高

    def findBestChess(self, data):  # AI入口
        self.reset()
        self.getMap(data)
        self.getEmptyPoint(data)
        score, move = self.score()
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
        map = self.map
        score = self.pos_score.copy()
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        final_score = []

        # 具体得分
        for i in range(8):
            m, n = dir[i]
            for j in range(len(self.empty_point)):
                x, y = self.empty_point[j]
                x += 4
                y += 4
                if map[x+m][y+n] == 2 and map[x+2*m][y+2*n] == 2 and map[x+3*m][y+3*n] == 2 and map[x+4*m][y+4*n] == 2:
                    score[x-4][y-4] += 50000
                elif map[x+m][y+n] == 1 and map[x+2*m][y+2*n] == 1 and map[x-m][y-n] == 1 and map[x-2*m][y-2*n] == 1:
                    score[x-4][y-4] += 7000
                elif map[x+m][y+n] == 1 and map[x+2*m][y+2*n] == 1 and map[x+3*m][y+3*n] == 1 and map[x+4*m][y+4*n] != 2:
                    score[x-4][y-4] += 7000
                elif map[x+m][y+n] == 1 and map[x+2*m][y+2*n] == 1 and map[x-m][y-n] == 1 and (map[x+3*m][y+3*n] == 0 or map[x-2*m][y-2*n] == 0):
                    score[x-4][y-4] += 7000
                elif map[x+m][y+n] == 2 and map[x+2*m][y+2*n] == 2 and map[x-m][y-n] == 2 and (map[x+3*m][y+3*n] == 0 or map[x-2*m][y-2*n] == 0):
                    score[x-4][y-4] += 1000
                elif map[x+m][y+n] == 2 and map[x+2*m][y+2*n] == 2 and map[x+3*m][y+3*n] == 2 and map[x+4*m][y+4*n] == 0:
                    score[x-4][y-4] += 1000
                elif map[x+m][y+n] == 2 and map[x+2*m][y+2*n] == 2 and map[x+3*m][y+3*n] == 0:
                    score[x-4][y-4] += 6
                elif map[x+m][y+n] == 1 and map[x+2*m][y+2*n] == 1 and map[x+3*m][y+3*n] == 1 and (map[x+4*m][y+4*n] == 2 or map[x+4*m][y+4*n] == 3):
                    score[x-4][y-4] += 5
                elif map[x+m][y+n] == 2 and map[x+2*m][y+2*n] == 2 and map[x+3*m][y+3*n] == 0:
                    score[x-4][y-4] += 4
                elif map[x+m][y+n] == 2 and map[x+2*m][y+2*n] == 2 and map[x+3*m][y+3*n] == 2 and (map[x+4*m][y+4*n] == 1 or map[x+4*m][y+4*n] == 3):
                    score[x-4][y-4] += 4
                elif map[x+m][y+n] == 2 and map[x+2*m][y+2*n] == 2 and (map[x+3*m][y+3*n] == 1 or map[x+3*m][y+3*n] == 3):
                    score[x-4][y-4] += 2
                elif map[x+m][y+n] == 2 and (map[x+2*m][y+2*n] == 1 or map[x+2*m][y+2*n] == 3):
                    score[x-4][y-4] += 0
                elif map[x+m][y+n] == 2:
                    score[x-4][y-4] += 2
                elif map[x+m][y+n] == 1:
                    score[x-4][y-4] += 0
                else:
                    score[x-4][y-4] += 0

        # 记录最终得分
        for j in range(len(self.empty_point)):
            x, y = self.empty_point[j]
            final_score.append((score[x][y], (x, y)))

        # 获取最高分
        best_move = max(final_score)
        return best_move
