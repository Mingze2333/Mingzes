from tkinter import *
from game import Game

class Screen:  # 窗口类
    def __init__(self):
        # 初始化
        self.root = Tk()
        self.game = Game()
        self.pos()
        self.move = False
        self.root.title('五子棋')

        # 绘制棋盘
        self.canvas = Canvas(self.root, width=626, height=626)
        self.canvas.pack()
        for i in self.point:
            self.canvas.create_line(i, 32, i, 592)
            self.canvas.create_line(32, i, 592, i)
        self.canvas.create_rectangle(148, 148, 156, 156, fill='black')
        self.canvas.create_rectangle(148, 468, 156, 476, fill='black')
        self.canvas.create_rectangle(308, 308, 316, 316, fill='black')
        self.canvas.create_rectangle(468, 148, 476, 156, fill='black')
        self.canvas.create_rectangle(468, 468, 476, 476, fill='black')

        # 绑定鼠标左键
        self.canvas.bind('<Button-1>', self.onclick)

        # 创建棋子列表
        self.pieces_b = []  #　黑棋
        self.pieces_w = []  #　白棋

    def mainloop(self):  # 主循环
        while True:
            # ai落子和检测胜负
            if self.move:
                # 检测1
                result = self.game.result()
                if result == 1:
                    self.over(1)
                    break
                # ai落子
                ai_pos = self.game.ai_move()
                self.pieces_w.append(self.get_point_pos[ai_pos])
                # 检测2
                result = self.game.result()
                if result == 2:
                    self.over(2)
                    break
                # 检测3
                result = self.game.result()
                if result == 3:
                    self.over(3)
                    break
                # 允许玩家落子
                self.move = False

            #  绘制棋子
            for piece in self.pieces_b:
                self.canvas.create_oval(piece[0]-16, piece[1]-16, piece[0]+16, piece[1]+16, fill='black')
            for piece in self.pieces_w:
                self.canvas.create_oval(piece[0] - 16, piece[1] - 16, piece[0] + 16, piece[1] + 16, fill='white')

            # 刷新屏幕
            try:
                self.root.update()
            except TclError:
                break

    def pos(self):  # 获取可落子点的坐标
        # x和y上的落子点的像素位置
        i = 32  # 1点的像素
        self.point = []
        while i <= 592:  # 15点的像素
            self.point.append(i)
            i += 40  # 每个点之间的像素

        # 利用字典一一对应，用一个列表记录每个点的像素坐标
        self.get_point_pos = {}  # pos --> point_pos
        self.get_pos = {}  # point_pos --> pos
        self.point_pos = []  # 像素坐标
        for y in range(15):
            for x in range(15):
                self.get_point_pos[(x, y)] = (self.point[x], self.point[y])
                self.get_pos[(self.point[x], self.point[y])] = (x, y)
                self.point_pos.append((self.point[x], self.point[y]))

    def onclick(self, event):  # 玩家落子
        # 初始化
        point_pos = ()

        # 监测鼠标事件
        for x, y in self.point_pos:
            if (x - 20 <= event.x < x + 20) and (y - 20 <= event.y < y + 20):
                point_pos = (x, y)

        # 返回结果
        pos = self.get_pos[point_pos]
        self.move = self.game.move(pos)
        if self.move:
            self.pieces_b.append(point_pos)

    def over(self, result):  # 结束窗口
        if result == 1:
            self.canvas.delete(ALL)
            self.canvas.create_text(313, 313, text=' 你赢了 ', font=('楷体', 100), fill='#CC3333')
        if result == 2:
            self.canvas.delete(ALL)
            self.canvas.create_text(313, 313, text='电脑获胜', font=('楷体', 100), fill='#CC3333')
        if result == 3:
            self.canvas.delete(ALL)
            self.canvas.create_text(313, 313, text='  平局  ', font=('楷体', 100), fill='#CC3333')
        self.root.mainloop()
