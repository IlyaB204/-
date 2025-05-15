import tkinter as tk
from tkinter import Canvas,BOTH, ttk,messagebox
import random

root = tk.Tk()
root.title('Хайнонские башни')

class Tower:
    def __init__(self, student):
        self.id = list(reversed(student + '0'))
        self.splind = self.create_sp()

    def create_sp(self):
        print('Вызван метод create_sp')
        self.splind = [self.create_disk(i, int(j)) for i,j in enumerate(self.id)]
        return  self.splind


    def create_disk(self,student, disk):
        return [student * 10 + i for i in range(disk, 0, -1)]

class Hanoi:
    spl = [[], [770, 575], [675, 575], [580, 575], [485, 575], [390, 575],
              [295, 575], [200, 575], [105, 575]]
    def __init__(self, master):
        self.master = master
        self.stud = '0'
        self.tower = Tower(self.stud)
        self.canvas = tk.Canvas(self.master, width=1100, height=900)
        self.selected_disk = None
        self.selected_spindle = None
        self.create_canvas()
        self.panel()
        self.canvas.pack(fill=BOTH, expand=1)
        self.canvas.bind("<Button-1>", self.on_click)


    def panel(self):
        btn_style = ttk.Style()
        btn_style.configure('TButton', width=20, height=50, background = '#783636')

        start_btn = ttk.Button(text='Start', style= 'TButton', command=self.start)
        start_btn.place(x=150, y=700)

        end_btn = ttk.Button(text='End', style='TButton')
        end_btn.place(x=600, y=700)

        self.entry = ttk.Entry(self.master)
        self.entry.place(x=383, y=780)

        save_btn = ttk.Button(self.master,text='Save', style='TButton',command=lambda :self.save_btn_command())
        save_btn.place(x=383, y=820)

    def create_canvas(self):
        self.canvas.create_rectangle(50, 600, 825, 585,width=3, outline="red")

        for i, j in enumerate(range(8,0,-1)):
            x1 = 100 + 95* i
            self.canvas.create_rectangle(x1, 585, x1 + 10, 305, width=3, outline="red")
            self.canvas.create_text(x1 + 4, 593, text=str(j), fill='black')

    def create_canvas_disk(self, data):
        print('Start Work')
        for i, new_data in enumerate(data):
            for j, disk in enumerate(new_data):
                x0 = self.spl[i][0]
                y0 = self.spl[i][1] - (j * 10)  # Позиция Y зависит от индекса диска
                color2 = self.random_colors()
                pol = disk // 2
                x0 -= pol

                # Создаем диск
                self.canvas.create_rectangle(x0, y0, x0 + disk, y0 + 10, fill=color2, tags='disk')

                # Создаем текст на диске
                self.canvas.create_text(x0 + pol, y0 + 5, text=disk, fill='black', tags='text_disk')  # Центрируем текст
        print('Метод create_canvas_disk закончил работу')

    def random_colors(self):
        return f'#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}'

    def delete_all(self):
        self.canvas.delete('disk')
        self.canvas.delete('text_disk')

    def start(self):
        self.delete_all()
        print('Метод create_sp вернул ответ')
        self.create_canvas_disk(self.tower.create_sp())


    def save_btn_command(self):
        value = self.entry.get()
        if len(value) > 8:
            messagebox.showinfo("Ошибка", "Размер ID больше 8 символов!")
            return
        else:
            self.stud = str(value)
            self.tower = Tower(value)

    def on_click(self, event):
        x=event.x
        spindle_index = None

        # Определяем, на какой шпиндель был совершен клик
        if x < 150:
            spindle_index = 8
        elif x < 250:
            spindle_index = 7
        elif x < 350:
            spindle_index = 6
        elif x < 450:
            spindle_index = 5
        elif x < 550:
            spindle_index = 4
        elif x < 650:
            spindle_index = 3
        elif x < 750:
            spindle_index = 2
        elif x < 850:
            spindle_index = 1
        if spindle_index is not None:
            if self.selected_disk is not None:
                if self.spl[self.selected_disk]:
                    self.selected_disk = self.spl[self.selected_disk].pop()
                    self.selected_spindle = spindle_index
                    self.start()
            else:
                if (not self.spl[spindle_index] or self.splindes[spindle_index][-1].size > self.selected_disk.size):
                    self.spl[spindle_index].append(self.selected_disk)  # Перемещаем диск на новый шпиндель
                    self.selected_disk = None  # Сбрасываем выбранный диск
                    self.start()






root.geometry('900x900')
app = Hanoi(root)
root.mainloop()