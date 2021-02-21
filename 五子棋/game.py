from ai import AI

class Game:  # 基础规则类
    def __init__(self):
        self.ai = AI()  # 初始化AI
        self.map = [[0 for x in range(15)] for y in range(15)]  # 构建棋盘二维列表

    def move(self, pos):  # 玩家落子
        while True:
            x, y = pos
            try:
                if 0 <= x <= 14 and 0 <= y <= 14:  # 判断是否能落子
                    if self.map[x][y] == 0:
                        self.map[x][y] = 1  # 落子（玩家落子为1）
                        return True
                return False
            except ValueError:
                continue

    def ai_move(self):  # 电脑落子
        move = AI.findBestChess(self.ai, self.map)
        x, y = move
        self.map[x][y] = 2  # 落子（电脑落子为2）
        return move

    def result(self):  # 胜负判断
        # 0为游戏中 1为玩家胜利 2为电脑胜利 3为平局
        # 1.判断横向五子
        for x in range(11):
            for y in range(15):
                if self.map[x][y] == 1\
                        and self.map[x+1][y] == 1\
                        and self.map[x+2][y] == 1\
                        and self.map[x+3][y] == 1\
                        and self.map[x+4][y] == 1:
                    return 1
                if self.map[x][y] == 2\
                        and self.map[x+1][y] == 2\
                        and self.map[x+2][y] == 2\
                        and self.map[x+3][y] == 2\
                        and self.map[x+4][y] == 2:
                    return 2

        # 2.判断纵向五子
        for x in range(15):
            for y in range(11):
                if self.map[x][y] == 1 \
                        and self.map[x][y+1] == 1\
                        and self.map[x][y+2] == 1\
                        and self.map[x][y+3] == 1\
                        and self.map[x][y+4] == 1:
                    return 1
                if self.map[x][y] == 2 \
                        and self.map[x][y+1] == 2 \
                        and self.map[x][y+2] == 2 \
                        and self.map[x][y+3] == 2 \
                        and self.map[x][y+4] == 2:
                    return 2

        # 3.判断左上-右下五子
        for x in range(11):
            for y in range(11):
                if self.map[x][y] == 1 \
                        and self.map[x+1][y+1] == 1 \
                        and self.map[x+2][y+2] == 1 \
                        and self.map[x+3][y+3] == 1 \
                        and self.map[x+4][y+4] == 1:
                    return 1
                if self.map[x][y] == 2 \
                        and self.map[x+1][y+1] == 2 \
                        and self.map[x+2][y+2] == 2 \
                        and self.map[x+3][y+3] == 2 \
                        and self.map[x+4][y+4] == 2:
                    return 2

        # 4.判断右上-左下五子
        for x in range(11):
            for y in range(11):
                if self.map[x+4][y] == 1 \
                        and self.map[x+3][y+1] == 1 \
                        and self.map[x+2][y+2] == 1 \
                        and self.map[x+1][y+3] == 1 \
                        and self.map[x][y+4] == 1:
                    return 1
                if self.map[x+4][y] == 2 \
                        and self.map[x+3][y+1] == 2 \
                        and self.map[x+2][y+2] == 2 \
                        and self.map[x+1][y+3] == 2 \
                        and self.map[x][y+4] == 2:
                    return 2

        # 5.棋盘全满平局
        for x in range(15):
            for y in range(15):
                if self.map[x][y] == 0:
                    return 0
        return 3
