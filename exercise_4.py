import tkinter as tk
from tkinter import messagebox



class Disk:
    def __init__(self, size):
        self.size = size
        # Генерация цвета для диска на основе его размера
        self.color = f'#{(size * 30) % 256:02x}{(size * 70) % 256:02x}{(size * 110) % 256:02x}'

class Hanoi:
    def __init__(self, master, numdisk):
        self.master = master
        self.numdisk = numdisk
        self.splindes = [[],[],[],[],[],[],[],[]]
        self.canvas = tk.Canvas(master, width=900, height=500)
        self.canvas.pack()
        self.selected_disk = None  # Переменная для хранения выбранного диска
        self.selected_spindle = None

        self.draw_splindes()
        self.create_disk()
        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        x = event.x
        spindle_index = None

        # Определяем, на какой шпиндель был совершен клик
        if x < 150:
            spindle_index = 0
        elif x < 250:
            spindle_index = 1
        elif x < 350:
            spindle_index = 2
        elif x < 450:
            spindle_index = 3
        elif x < 550:
            spindle_index = 4
        elif x < 650:
            spindle_index = 5
        elif x < 750:
            spindle_index = 6
        elif x < 850:
            spindle_index = 7

        if spindle_index is not None:
            if self.selected_disk is None:
                if self.splindes[spindle_index]:
                    self.selected_disk = self.splindes[spindle_index].pop()
                    self.selected_spindle = spindle_index
                    self.draw_splindes()
            else:
                if (not self.splindes[spindle_index] or
                        self.splindes[spindle_index][-1].size > self.selected_disk.size):
                    self.splindes[spindle_index].append(self.selected_disk)  # Перемещаем диск на новый шпиндель
                    self.selected_disk = None  # Сбрасываем выбранный диск
                    self.draw_splindes()  # Перерисовываем шпиндели и диски
                    if self.check_win():  # Проверяем, выиграл ли игрок
                        messagebox.showinfo("Поздравляем!", "Вы выиграли!")



    def draw_splindes(self):
        self.canvas.delete('all')

        splind_width = 10
        splind_height = 400
        splind_position = [100,200,300,400,500,600,700,800]

        for i in range(8):
            x = splind_position[i]
            self.canvas.create_rectangle(x - splind_width / 2, 100, x + splind_width / 2, 400, fill='red')
            for j, disk in enumerate(self.splindes[i]):
                disk_width = disk.size * 20  # Ширина диска в зависимости от его размера
                disk_height = 20  # Высота диска
                disk_x1 = x - disk_width / 2  # Левый край диска
                disk_x2 = x + disk_width / 2  # Правый край диска
                disk_y = 400 - (j + 1) * disk_height  # Вертикальная позиция диска
                self.canvas.create_rectangle(disk_x1, disk_y, disk_x2, disk_y + disk_height, fill=disk.color)

    def create_disk(self):
        for i in range(self.numdisk, 0, -1):
            disk = Disk(i)  # Создаем новый диск
            self.splindes[0].append(disk)
        self.draw_splindes()

    def check_win(self):
        return len(self.splindes[7]) == self.numdisk  # Проверяем, находятся ли все диски на третьем шпинделе


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Башни Ханой')
    app = Hanoi(root, numdisk=8)
    root.mainloop()