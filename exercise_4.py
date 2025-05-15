import tkinter as tk
from tkinter import messagebox, simpledialog


class Disk:
    def __init__(self, size, spindle_index, position):
        self.size = size
        self.spindle_index = spindle_index
        self.position = position
        self.color = f'#{(size * 30) % 256:02x}{(size * 70) % 256:02x}{(size * 110) % 256:02x}'
        self.diameter = self.calculate_diameter()

    def calculate_diameter(self):
        return self.spindle_index * 10 + self.position


class Hanoi:
    def __init__(self, master):
        self.master = master
        self.splindes = [[] for _ in range(8)]
        self.canvas = tk.Canvas(master, width=900, height=500)
        self.canvas.pack()
        self.selected_disk = None
        self.selected_spindle = None

        self.ask_for_disks()
        self.draw_splindes()
        self.canvas.bind("<Button-1>", self.on_click)

    def ask_for_disks(self):
        while True:
            user_input = simpledialog.askstring("Ввод", "Введите 8-значное число (каждая цифра - количество дисков на шпинделе):")
            if user_input and len(user_input) == 8 and user_input.isdigit():
                for i in range(8):
                    num_disks = int(user_input[i])
                    for size in range(num_disks, 0, -1):
                        disk = Disk(size, i, num_disks - size + 1)
                        self.splindes[i].append(disk)
                break
            else:
                messagebox.showerror("Ошибка", "Введите корректное 8-значное число.")

    def on_click(self, event):
        x = event.x
        spindle_index = None

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
                # Выбор диска
                if self.splindes[spindle_index]:
                    self.selected_disk = self.splindes[spindle_index].pop()
                    self.selected_spindle = spindle_index
                    self.draw_splindes()
            else:
                # Проверка возможности перемещения диска
                if (self.splindes[spindle_index][-1].size > self.selected_disk.size):
                    # Перемещение диска
                    self.splindes[spindle_index].append(self.selected_disk)
                    self.selected_disk = None
                    self.draw_splindes()
                    if self.check_win():
                        messagebox.showinfo("Поздравляем!", "Вы выиграли!")
                else:
                    # Если перемещение невозможно, выводим сообщение
                    messagebox.showwarning("Ошибка", "Нельзя переместить диск на больший диск.")


    def draw_splindes(self):
        self.canvas.delete('all')

        splind_width = 10
        splind_height = 400
        splind_position = [100, 200, 300, 400, 500, 600, 700, 800]

        for i in range(8):
            x = splind_position[i]
            self.canvas.create_rectangle(x - splind_width / 2, 100, x + splind_width / 2, 400, fill='red')
            for j, disk in enumerate(self.splindes[i]):
                disk_width = disk.size * 20
                disk_height = 20
                disk_x1 = x - disk_width / 2
                disk_x2 = x + disk_width / 2
                disk_y = 400 - (j + 1) * disk_height

                # Рисуем диск
                self.canvas.create_rectangle(disk_x1, disk_y, disk_x2, disk_y + disk_height, fill=disk.color)
                # Отображаем диаметр на диске
                diameter_text = str(disk.diameter)
                text_x = x
                text_y = disk_y + disk_height / 2
                self.canvas.create_text(text_x, text_y, text=diameter_text, fill="black")

    def check_win(self):
        return len(self.splindes[7]) == sum(len(spindle) for spindle in self.splindes) - len(self.splindes[0])

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Башни Ханой')
    app = Hanoi(root)
    root.mainloop()
