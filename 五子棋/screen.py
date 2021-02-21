# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit
from game import Game

class Screen():  # 窗口类
    def __init__(self):  # 主窗口
        # 初始化
        pygame.init()
        self.game = Game()
        self.pos()
        self.move = False

        # 设置窗口
        screen = pygame.display.set_mode((626, 626), 0)
        pygame.display.set_caption('五子棋')

        # 加载图片和字体
        bg = pygame.image.load('bg.gif').convert()
        piece_w = pygame.image.load('piece_w.gif').convert_alpha()
        piece_b = pygame.image.load('piece_b.gif').convert_alpha()
        self.font = pygame.font.Font('simkai.ttf', 100)

        # 创建棋子列表
        self.pieces_b = []
        self.pieces_w = []

        # 主循环
        while True:
            # 监测事件
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if event.button == 1:
                        for x, y in self.point_pos:
                            if (x-20 <= mouse_pos[0] < x+20) and (y-20 <= mouse_pos[1] < y+20):
                                self.onclick((x, y))

            # 绘制屏幕内容
            screen.blit(bg, (0, 0))

            for piece in self.pieces_b:
                screen.blit(piece_b, (piece[0]-16, piece[1]-16))
            for piece in self.pieces_w:
                screen.blit(piece_w, (piece[0]-16, piece[1]-16))

            # ai落子和检测胜负
            if self.move:
                self.move = False

                # 检测1
                result = self.game.result()
                if result == 1:
                    self.over(1)

                # ai落子
                ai_pos = self.game.ai_move()
                self.pieces_w.append(self.get_point_pos[ai_pos])

                # 检测2
                result = self.game.result()
                if result == 2:
                    self.over(2)

                # 检测3
                result = self.game.result()
                if result == 3:
                    self.over(3)

            # 刷新屏幕
            pygame.display.update()

    def pos(self):  # 获取可落子点的坐标
        # x和y上的落子点的像素位置
        i = 32
        point = []
        while i <= 592:
            point.append(i)
            i += 40
            
        # 利用字典一一对应，用一个列表记录每个点的坐标
        self.get_point_pos = {}
        self.get_pos = {}
        self.point_pos = []
        for y in range(15):
            for x in range(15):
                        self.get_point_pos[(x, y)] = (point[x], point[y])
                        self.get_pos[(point[x], point[y])] = (x, y)
                        self.point_pos.append((point[x], point[y]))

    def onclick(self, point_pos):  # 玩家落子
        pos = self.get_pos[point_pos]
        self.move = self.game.move(pos)
        if self.move:
            self.pieces_b.append(point_pos)

    def over(self, result):  # 结束窗口
        # 设置窗口
        over_screen = pygame.display.set_mode((400, 100), 0)
        pygame.display.set_caption('游戏结束')
        over_screen.fill((255, 255, 255))

        # 设置文字
        t1 = self.font.render(' 你赢了 ', True, (204, 51, 51))
        t2 = self.font.render('电脑获胜', True, (204, 51, 51))
        t3 = self.font.render('  平局  ', True, (204, 51, 51))

        # 结束窗口循环
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            # 绘制文字
            if result == 1:
                over_screen.blit(t1, (0, 0))
            if result == 2:
                over_screen.blit(t2, (0, 0))
            if result == 3:
                over_screen.blit(t3, (0, 0))

            # 刷新屏幕
            pygame.display.update()
