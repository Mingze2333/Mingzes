class AI:
    def __init__(self):
        self.map = [[3 for x in range(23)] for y in range(23)]
        self.pos_score = [[(7-max(abs(x-7), abs(y-7))) for x in range(15)] for y in range(15)]
        self.best_score = []
        self.empty_point = []  # (x, y)

    def findBestChess(self, data):
        self.map = [[3 for x in range(23)] for y in range(23)]
        self.empty_point.clear()
        self.best_score.clear()

        self.getMap(data)
        self.getEmptyPoint(data)

        score, move = self.score()
        print(score)
        return move

    def getMap(self, data):
        for x in range(4, 19):
            for y in range(4, 19):
                self.map[x][y] = data[x-4][y-4]

    def getEmptyPoint(self, data):
        for x in range(15):
            for y in range(15):
                if data[x][y] == 0:
                    self.empty_point.append((x, y))

    def score(self):
        map = self.map
        score = self.pos_score.copy()
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, 1), (-1, -1)]

        for i in range(8):
            m, n = dir[i]
            for j in range(len(self.empty_point)):
                x, y = self.empty_point[j]
                x += 4
                y += 4

                if map[x+m][y+n] == 2 and map[x+2*m][y+2*n] == 2 and map[x+3*m][y+3*n] == 2 and map[x+4*m][y+4*n] == 2:
                    score[x-4][y-4] += 10000
                elif map[x+m][y+n] == 1 and map[x+2*m][y+2*n] == 1 and map[x+3*m][y+3*n] == 1 and map[x+4*m][y+4*n] == 1:
                    score[x-4][y-4] += 1010
                elif map[x+m][y+n] == 1 and map[x+2*m][y+2*n] == 1 and map[x+3*m][y+3*n] == 1 and (map[x+4*m][y+4*n] == 0 or map[x-4][y] == 1):
                    score[x-4][y-4] += 1000
                elif map[x+m][y+n] == 2 and map[x+2*m][y+2*n] == 2 and map[x+3*m][y+3*n] == 2 and map[x+4*m][y+4*n] == 0:
                    score[x-4][y-4] += 100
                elif map[x+m][y+n] == 2 and map[x+2*m][y+2*n] == 2 and map[x+3*m][y+3*n] == 0:
                    score[x-4][y-4] += 6
                elif map[x+m][y+n] == 1 and map[x+2*m][y+2*n] == 1 and map[x+3*m][y+3*n] == 1 and (map[x+4*m][y+4*n] == 2 or map[x+4*m][y+4*n] == 3):
                    score[x-4][y-4] += 5
                elif map[x+m][y+n] == 2 and map[x+2*m][y+2*n] == 2 and map[x+3*m][y+3*n] == 2 and (map[x+4*m][y+4*n] == 1 or map[x+4*m][y+4*n] == 3):
                    score[x-4][y-4] += 4
                elif map[x+m][y+n] == 2 and map[x+2*m][y+2*n] == 2 and (map[x+3*m][y+3*n] == 1 or map[x+3*m][y+3*n] == 3):
                    score[x-4][y-4] += 3
                elif map[x+m][y+n] == 2 and (map[x+2*m][y+2*n] == 1 or map[x+2*m][y+2*n] == 3):
                    score[x-4][y-4] += 0
                elif map[x+m][y+n] == 2:
                    score[x-4][y-4] += 2
                elif map[x+m][y+n] == 1:
                    score[x-4][y-4] += -2
                else:
                    score[x-4][y-4] += 0

        for j in range(len(self.empty_point)):
            x, y = self.empty_point[j]
            self.best_score.append((score[x][y], (x, y)))

        best_move = max(self.best_score)
        return best_move
