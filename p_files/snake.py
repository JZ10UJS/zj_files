# -*- coding:utf-8 -*-

from turtle import Vec2D
import Tkinter as tk, random, itertools

kGridWidth, kGridHeight, kGridPixels = 15, 15, 20  # 网格尺寸、网格像素数
kCanvasWidth, kCanvasHeight = kGridWidth * kGridPixels, kGridHeight * kGridPixels  # 画布尺寸
kDirs = {'Up': Vec2D(0, -1), 'Left': Vec2D(-1, 0), 'Down': Vec2D(0, 1), 'Right': Vec2D(1, 0)}  # 方向
kSceneStart, kScenePlay, kSceneOver = 0, 1, 2  # 场景
kUpdateDelay = 500  # 更新间隔（ms）

class SnakeGame:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=kCanvasWidth, height=kCanvasHeight, bg='gray')
        self.canvas.pack()
        self.root.bind('<KeyPress>', self.update)
        self.valid_pos = set(map(lambda t: Vec2D(*t), itertools.product(range(kGridWidth), range(kGridHeight))))  # 有效网格坐标集合
        self.rand_pos = lambda w, h: Vec2D(random.randint(0, w - 1), random.randint(0, h - 1))  # 生成随机网格坐标
        self.food = (None, self.canvas.create_oval(0, 0, 0, 0, fill='green'))  # 食物：(网格坐标, 图形对象)
        self.snake_dir = None  # 蛇头方向：Vec2D(x, y)
        self.snake_bodys = []  # 蛇身：[(网格坐标,图形对象), ...]
        self.scene = kSceneStart  # 场景编号
        self.score = 0  # 分数
        self.update_funcs = [self.update_gamestart, self.update_gameplay, self.update_gameover]  # 场景更新函数
        self.next_update = self.root.after(kUpdateDelay, self.update)  # 延迟执行下一次更新

    def next_food(self):  # 生成下一个食物
        while True:
            pos = self.rand_pos(kGridWidth, kGridHeight)
            if pos not in map(lambda b: b[0], self.snake_bodys):  # 判定是否与蛇身冲突
                self.canvas.coords(self.food[1], (pos[0] * kGridPixels + 2, pos[1] * kGridPixels + 2,
                                                  pos[0] * kGridPixels + kGridPixels, pos[1] * kGridPixels + kGridPixels))
                self.food = (pos, self.food[1])
                return

    def move(self):  # 移动蛇头
        new_pos = self.snake_bodys[0][0] + self.snake_dir
        if new_pos not in self.valid_pos or new_pos in map(lambda b: b[0], self.snake_bodys[:-1]):  # 测试新的蛇头位置是否有效
            return False
        if new_pos == self.food[0]:  # 吃到食物时
            self.snake_bodys.insert(0, (new_pos, self.canvas.create_oval(new_pos[0] * kGridPixels + 2, new_pos[1] * kGridPixels + 2,
                                                                         new_pos[0] * kGridPixels + kGridPixels, new_pos[1] * kGridPixels + kGridPixels,
                                                                         fill='red', tags='SnakeBodys')))
            self.next_food()
            self.score += 1
        else:
            self.canvas.coords(self.snake_bodys[-1][1], (new_pos[0] * kGridPixels + 2, new_pos[1] * kGridPixels + 2,
                                                         new_pos[0] * kGridPixels + kGridPixels, new_pos[1] * kGridPixels + kGridPixels))
            self.snake_bodys.insert(0, (new_pos, self.snake_bodys.pop()[1]))  # 直接将蛇尾移动至新蛇头
        return True

    def update(self, event=None):
        self.update_funcs[self.scene](event)  # 执行当前场景的更新函数

    def update_gamestart(self, event):  # 游戏开始场景
        if event and event.keysym == 'Return':  # 按下回车
            self.canvas.delete('GameStartString')
            self.snake_dir = random.choice(kDirs.values())
            head = self.rand_pos(kGridWidth, kGridHeight)
            self.snake_bodys = [(head, self.canvas.create_oval(head[0] * kGridPixels + 2, head[1] * kGridPixels + 2,
                                                               head[0] * kGridPixels + kGridPixels, head[1] * kGridPixels + kGridPixels,
                                                               fill='red', tags='SnakeBodys'))]
            self.next_food()
            self.scene = kScenePlay
            self.next_update = self.root.after(kUpdateDelay, self.update)
        elif not self.canvas.find_withtag('GameStartString'):  # 画面初始化
            self.canvas.create_text((kCanvasWidth / 2, kCanvasHeight / 6 * 2), text='Welcome to the simple snake game.', tags='GameStartString')
            self.canvas.create_text((kCanvasWidth / 2, kCanvasHeight / 6 * 3), text='Move the snake with <Up, Left, Down, Right>.', tags='GameStartString')
            self.canvas.create_text((kCanvasWidth / 2, kCanvasHeight / 6 * 4), text='Please press <Enter> to start.', tags='GameStartString')

    def update_gameplay(self, event):  # 游戏进行场景
        try:
            if event and event.keysym in kDirs and kDirs[event.keysym] + self.snake_dir != Vec2D(0, 0):  # 按下方向键且与当前方向不相反时
                self.root.after_cancel(self.next_update)
                self.snake_dir = kDirs[event.keysym]
                if not self.move():
                    raise  # 懒
            elif not event:  # 自动更新时
                if not self.move():
                    raise
            else:  # 忽略其他按键
                return
        except:  # 死亡
            self.canvas.delete('SnakeBodys')
            self.canvas.coords(self.food[1], (0, 0, 0, 0))
            self.scene = kSceneOver
        self.next_update = self.root.after(kUpdateDelay, self.update)  # 延迟执行下一次更新

    def update_gameover(self, event):  # 游戏结束场景
        if event and event.keysym == 'Escape':  # 按下Esc
            self.canvas.delete('GameOverString')
            self.scene = kSceneStart
            self.next_update = self.root.after(kUpdateDelay, self.update)
        elif not self.canvas.find_withtag('GameOverString'):  # 画面初始化
            self.canvas.create_text((kCanvasWidth / 2, kCanvasHeight / 5 * 2), text='Your score is: %d' % self.score, tags='GameOverString')
            self.canvas.create_text((kCanvasWidth / 2, kCanvasHeight / 5 * 3), text='Please press <Esc> to restart.', tags='GameOverString')

if __name__ == '__main__':
    SnakeGame().root.mainloop()
