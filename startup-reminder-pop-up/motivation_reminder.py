import tkinter as tk
from tkinter import font
import time
import threading
import math
import random


class MotivationWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Daily Motivation")

        # 窗口设置
        self.window_width = 600
        self.window_height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2
        self.root.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

        # 窗口样式
        self.root.overrideredirect(True)  # 无边框窗口，更现代
        self.root.attributes('-topmost', True)
        self.root.configure(bg='#1a1a2e')

        # 设置圆角效果（Windows）
        try:
            self.root.attributes('-transparentcolor', '#1a1a2e')
        except:
            pass

        # 创建画布
        self.canvas = tk.Canvas(
            self.root,
            width=self.window_width,
            height=self.window_height,
            bg='#0f0f1e',
            highlightthickness=0
        )
        self.canvas.pack(fill='both', expand=True)

        # 动画相关
        self.opacity = 0
        self.particles = []
        self.meteors = []  # 初始化流星列表

        # 初始化粒子和流星
        self.init_particles()
        self.init_meteors()  # 调用流星初始化

        # 绘制界面
        self.draw_background()
        self.draw_content()

        # 启动动画
        self.fade_in()
        self.animate_particles()
        self.animate_meteors()  # 启动流星动画

        # 自动关闭定时器
        threading.Thread(target=self.auto_close, daemon=True).start()

    def init_particles(self):
        """初始化粒子效果"""
        for _ in range(30):
            self.particles.append({
                'x': random.randint(0, self.window_width),
                'y': random.randint(0, self.window_height),
                'size': random.randint(2, 4),
                'speed': random.uniform(0.3, 0.8),
                'opacity': random.uniform(0.3, 0.7)
            })

    def init_meteors(self):
        """初始化流星"""
        # 创建3个流星
        for i in range(3):
            self.create_meteor()

    def create_meteor(self):
        """创建单个流星"""
        meteor = {
            'x': random.randint(self.window_width // 2, self.window_width),
            'y': random.randint(-50, self.window_height // 3),
            'length': random.randint(60, 120),
            'speed': random.uniform(2, 4),
            'angle': random.uniform(45, 50),  # 流星角度
            'opacity': random.uniform(0.6, 1.0),
            'delay': random.randint(0, 100)  # 随机延迟
        }
        self.meteors.append(meteor)

    def draw_background(self):
        """绘制背景"""
        # 深色渐变背景
        for i in range(self.window_height):
            ratio = i / self.window_height
            # 从深紫到深蓝的渐变
            r = int(15 + (26 - 15) * ratio)
            g = int(15 + (35 - 15) * ratio)
            b = int(30 + (62 - 30) * ratio)
            color = f'#{r:02x}{g:02x}{b:02x}'
            self.canvas.create_line(0, i, self.window_width, i, fill=color, width=1)

        # 添加光晕效果
        self.canvas.create_oval(
            -100, -100, 200, 200,
            fill='', outline='#6c5ce7', width=2, dash=(10, 5)
        )
        self.canvas.create_oval(
            self.window_width - 200, self.window_height - 200,
            self.window_width + 100, self.window_height + 100,
            fill='', outline='#a29bfe', width=2, dash=(10, 5)
        )

        # 中心装饰圆环
        center_x, center_y = self.window_width // 2, 120
        for i in range(3):
            radius = 70 + i * 15
            self.canvas.create_oval(
                center_x - radius, center_y - radius,
                center_x + radius, center_y + radius,
                outline=f'#{"6c5ce7" if i % 2 == 0 else "a29bfe"}',
                width=1,
                dash=(8, 8)
            )

    def draw_content(self):
        """绘制文字内容"""
        center_x = self.window_width // 2

        # 主标题（中文）
        title_font = font.Font(family="Microsoft YaHei UI", size=25, weight="bold")
        self.canvas.create_text(
            center_x, 200,
            text="You can input text within it.",
            font=title_font,
            fill='#ffffff',
            tags='title'
        )

        # 副标题（英文）
        subtitle_font = font.Font(family="Segoe UI", size=11, slant="italic")
        self.canvas.create_text(
            center_x, 245,
            text="Do you want to get stuck in the quagmire of embedded systems?",
            font=subtitle_font,
            fill='#b8b8d1',
            tags='subtitle'
        )

        # 底部激励语
        quote_font = font.Font(family="Segoe UI", size=10)
        self.canvas.create_text(
            center_x, 290,
            text="You can input text within it.",
            font=quote_font,
            fill='#8b8ba3'
        )

        # 关闭按钮
        self.draw_close_button()

    def draw_close_button(self):
        """绘制现代风格关闭按钮"""
        btn_x, btn_y = self.window_width // 2, 340

        # 按钮文字
        text = "You can input text within it."
        btn_font = font.Font(family="Microsoft YaHei UI", size=10, weight="bold")

        # 根据文字宽度动态调整按钮宽度
        text_width = btn_font.measure(text)
        padding = 30  # 两侧额外留白
        btn_width = text_width + padding
        btn_height = 36

        # 按钮背景
        self.canvas.create_rectangle(
            btn_x - btn_width // 2, btn_y - btn_height // 2,
            btn_x + btn_width // 2, btn_y + btn_height // 2,
            fill='#6c5ce7',
            outline='#a29bfe',
            width=2,
            tags='btn_bg'
        )

        # 按钮文字
        self.canvas.create_text(
            btn_x, btn_y,
            text=text,
            font=btn_font,
            fill='#ffffff',
            tags='btn_text'
        )

        # 绑定事件
        for tag in ("btn_bg", "btn_text"):
            self.canvas.tag_bind(tag, "<Enter>", self.on_button_enter)
            self.canvas.tag_bind(tag, "<Leave>", self.on_button_leave)
            self.canvas.tag_bind(tag, "<Button-1>", lambda e: self.fade_out())

        # 鼠标样式
        self.canvas.tag_bind('btn_bg', '<Enter>', lambda e: self.canvas.config(cursor='hand2'))
        self.canvas.tag_bind('btn_bg', '<Leave>', lambda e: self.canvas.config(cursor=''))

    def on_button_enter(self, event):
        """按钮悬停效果"""
        self.canvas.itemconfig('btn_bg', fill='#7c6cf7', outline='#b8b0ff')

    def on_button_leave(self, event):
        """按钮离开效果"""
        self.canvas.itemconfig('btn_bg', fill='#6c5ce7', outline='#a29bfe')

    def animate_meteors(self):
        """流星动画"""
        self.canvas.delete('meteor')

        for meteor in self.meteors:
            if meteor['delay'] > 0:
                meteor['delay'] -= 1
                continue

            # 计算流星轨迹
            angle_rad = math.radians(meteor['angle'])
            dx = meteor['speed'] * math.cos(angle_rad)
            dy = meteor['speed'] * math.sin(angle_rad)

            meteor['x'] -= dx
            meteor['y'] += dy

            # 重置流星
            if meteor['x'] < -100 or meteor['y'] > self.window_height + 100:
                meteor['x'] = random.randint(self.window_width // 2, self.window_width + 50)
                meteor['y'] = random.randint(-50, self.window_height // 3)
                meteor['length'] = random.randint(60, 120)
                meteor['delay'] = random.randint(100, 300)
                continue

            # 绘制流星（渐变尾迹）
            x1, y1 = meteor['x'], meteor['y']
            x2 = x1 + meteor['length'] * math.cos(angle_rad)
            y2 = y1 - meteor['length'] * math.sin(angle_rad)

            # 创建渐变效果
            segments = 10
            for i in range(segments):
                ratio = i / segments
                x_start = x1 + (x2 - x1) * ratio
                y_start = y1 + (y2 - y1) * ratio
                x_end = x1 + (x2 - x1) * (ratio + 1 / segments)
                y_end = y1 + (y2 - y1) * (ratio + 1 / segments)

                opacity = int((1 - ratio) * meteor['opacity'] * 255)
                opacity = max(0, min(255, opacity))  # 确保在0-255范围内
                blue = max(0, min(255, opacity + 80))
                color = f'#{opacity:02x}{opacity:02x}{blue:02x}'
                width = max(1, int((1 - ratio) * 3))

                self.canvas.create_line(
                    x_start, y_start, x_end, y_end,
                    fill=color, width=width, tags='meteor'
                )

        self.root.after(30, self.animate_meteors)

    def animate_particles(self):
        """粒子动画"""
        self.canvas.delete('particle')

        for particle in self.particles:
            # 更新位置
            particle['y'] -= particle['speed']

            # 重置粒子
            if particle['y'] < 0:
                particle['y'] = self.window_height
                particle['x'] = random.randint(0, self.window_width)

            # 绘制粒子（修复颜色计算）
            opacity = int(particle['opacity'] * 255)
            blue = max(0, min(255, opacity + 50))  # 确保蓝色通道不超255
            color = f'#{opacity:02x}{opacity:02x}{blue:02x}'
            self.canvas.create_oval(
                particle['x'], particle['y'],
                particle['x'] + particle['size'], particle['y'] + particle['size'],
                fill=color,
                outline='',
                tags='particle'
            )

        # 继续动画
        self.root.after(50, self.animate_particles)

    def fade_in(self):
        """淡入动画"""
        if self.opacity < 1:
            self.opacity += 0.05
            self.root.attributes('-alpha', self.opacity)
            self.root.after(30, self.fade_in)

    def fade_out(self):
        """淡出动画"""
        if self.opacity > 0:
            self.opacity -= 0.1
            self.root.attributes('-alpha', self.opacity)
            self.root.after(20, self.fade_out)
        else:
            self.root.destroy()

    def auto_close(self):
        """自动关闭"""
        time.sleep(10)
        try:
            self.fade_out()
        except:
            pass

    def run(self):
        """运行窗口"""
        self.root.mainloop()


if __name__ == "__main__":
    app = MotivationWindow()
    app.run()