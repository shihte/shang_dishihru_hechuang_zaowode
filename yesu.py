import random
import turtle
from PIL import Image
import os
import tkinter as tk

# 標籤列表
tag = [
    "菜","gay","智慧法障","鍵盤俠血統","老司機",
    "中二","迷因","諧音梗","反骨","裸照外流風險",
]

# 全域變數，用於存儲輸入的文字
global_text = ""

def open_yesu():
    screen = turtle.Screen()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "yesu.gif")
    if os.path.exists(image_path):
        img = Image.open(image_path)
        width, height = img.size
        screen.setup(width, height)
        screen.bgpic(image_path)
    else:
        print("圖片 'yesu.gif' 不存在，請確保檔案在正確的位置。")
        screen.setup(800, 600)
    return screen

def init_turtle(width, height, title="損友是如何創造我的", bg_color="white"):
    screen = open_yesu()
    screen.title(title)
    t = turtle.Turtle()
    t.speed(0)  # 最快的繪圖速度
    t.hideturtle()
    return screen, t

def write_chinese_message(t):
    t.clear()  # 清除之前的內容
    t.color("black")
    t.penup()
    t.goto(-250, 280)
    message = "損友是如何創造我的"
    font_size = 36
    font = ("Arial", font_size, "normal")
    for char in message:
        t.write(char, font=font, align="center")
        t.forward(font_size + 10)

def random_tag():
    random_indices = random.sample(range(len(tag)), 3)
    point1 = random.randint(1, 98)
    point2 = random.randint(point1 + 1, 99)
    percentage1 = point1
    percentage2 = point2 - point1
    percentage3 = 100 - point2
    result = [
        f"{percentage1}% 的 {tag[random_indices[0]]}",
        f"{percentage2}% 的 {tag[random_indices[1]]}",
        f"{percentage3}% 的 {tag[random_indices[2]]}"
    ]
    return result

def ouput(screen, text, title_turtle, content_turtle):
    content_turtle.clear()  # 只清除內容，不清除背景
    write_chinese_message(title_turtle)  # 重新寫入標題
    tags = random_tag()
    
    content_turtle.speed(0)  # 最快的繪圖速度
    content_turtle.penup()
    content_turtle.color("black")
    
    start_y = screen.window_height() / 2 - 150
    
    content_turtle.goto(-350, start_y)
    content_turtle.write(f"{text}在損友眼中是由：", align="left", font=("Arial", 20, "normal"))
    
    for i, tag_text in enumerate(tags):
        content_turtle.goto(-300, start_y - 40 - i * 30)
        content_turtle.write(tag_text, align="left", font=("Arial", 16, "normal"))
    
    content_turtle.goto(-350, start_y - 40 - len(tags) * 30)
    content_turtle.write("組成", align="left", font=("Arial", 20, "normal"))

def create_input_box(screen, title_turtle, content_turtle):
    global global_text
    canvas = screen.getcanvas()
    
    entry = tk.Entry(canvas.master, width=30)
    entry.insert(0, "請輸入一個名字")
    entry.bind("<FocusIn>", lambda args: entry.delete('0', 'end') if entry.get() == "請輸入一個名字" else None)
    canvas.create_window(0, screen.window_height()/2 - 70, window=entry)
    
    def submit():
        global global_text
        global_text = entry.get()
        if global_text and global_text != "請輸入一個名字":
            ouput(screen, global_text, title_turtle, content_turtle)
            entry.delete(0, 'end')
            entry.insert(0, "請輸入一個名字")
        print(f"全域變數 global_text 的值為: {global_text}")
    
    button = tk.Button(canvas.master, text="開始計算", command=submit)
    canvas.create_window(0, screen.window_height()/2 - 40, window=button)

def main():
    global global_text
    screen, title_turtle = init_turtle(800, 600, "損友是如何創造我的", "white")
    content_turtle = turtle.Turtle()
    content_turtle.hideturtle()
    content_turtle.speed(0)
    write_chinese_message(title_turtle)
    create_input_box(screen, title_turtle, content_turtle)
    screen.mainloop()

if __name__ == "__main__":
    main()