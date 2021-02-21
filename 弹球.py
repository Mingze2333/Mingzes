import os
from tkinter import *
import random
import time

# 球类行为
class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,40,40,fill=color)
        self.canvas.move(self.id,480,200)
        self.x = 0
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.canvas.bind_all("<Return>", self.starts)

    # 球与拍碰撞检测函数
    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if (pos[2] >= paddle_pos[0]) and (pos[0] <= paddle_pos[2]):
            if (pos[3] >= paddle_pos[1]) and (pos[3] <= paddle_pos[3]):
                return True
        return False

    # 球碰撞行为函数
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 6
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos):
            self.y = -6
            canvas.itemconfig(scoreText, text="击球数：%d" %getScore())
        if pos[0] <= 0:
            self.x = 6
        if pos[2] >= self.canvas_width:
            self.x = -6

    # 开始游戏函数
    def starts(self,evt):
        self.canvas.itemconfig(startText, state="hidden")
        starts = [-6, 6]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -6

# 拍类行为
class Paddle:
    def __init__(self,canvas,color):
        self.canvas =canvas
        self.id = canvas.create_rectangle(0,0,200,20,fill=color)
        self.canvas.move(self.id,400,650)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        # 绑定按键
        self.canvas.bind_all("<KeyPress-Left>",self.left)
        self.canvas.bind_all("<KeyPress-Right>", self.right)

    # 拍碰撞行为函数
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] == 0:
            self.x = 0
        if pos[0] < 0:
            self.x = 4
        if pos[2] == self.canvas_width:
            self.x = 0
        if pos[2] > self.canvas_width:
            self.x = -4

    # 拍控制函数
    def left(self,evt):
        self.x = -4

    def right(self,evt):
        self.x = 4

# 得分函数
def getScore():
    global score
    score = score+1
    return(score)

# 重新开始函数
def restarts(evt):
    python = sys.executable
    os.execl(python,python,*sys.argv)

# 退出函数
def sysquit():
    global destroy
    destroy = True

# 生成窗口
tk = Tk()
tk.title("弹球")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=1000,height=800,bd=0,highlightthickness=0)
canvas.pack()
tk.update()

# 绑定关闭窗口按钮
tk.protocol("WM_DELETE_WINDOW",sysquit)

# 初始化变量
score = 0
destroy = False

#游戏内文本显示
gameoverText = canvas.create_text(500,400,fill="red",font=("Times",30),state="hidden")
startText = canvas.create_text(500,500,text="按回车开始游戏",fill="red",font=("Times",30),state="normal")
scoreText = canvas.create_text(920,30,text="击球数：0",font=("Times",15))

paddle = Paddle(canvas,"black")
ball = Ball(canvas,paddle,"red")

while True:
    # 球触底检测
    if ball.hit_bottom:
        time.sleep(1)
        canvas.itemconfig(gameoverText,text="    GAME OVER\n你的击球数为：%d\n 按回车重新开始"%score,state="normal")
        canvas.bind_all("<Return>", restarts)
    else:
        ball.draw()
        paddle.draw()

    # 关闭窗口检测
    if destroy:
        break

    # 保持窗口存在
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)