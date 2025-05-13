import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Хонойские башни')
root.geometry('1100x700')


class Disk:
    def __init__(self, size):
        self.size = size
        self.color = f'#{(size * 30) % 256:02x}{(size * 70) % 256:02x}{(size * 110) % 256:02x}'

class Tower:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=1000, height=600, bg = 'white')
        self.canvas.pack()

        self.splindes = [[],[],[],[],[],[],[],[]]
        self.numdisk_val = 0

        self.entry = tk.Entry()
        self.start_btn = tk.Button(text='Начать', command=self.get_id)
        self.entry.pack(side = tk.LEFT)
        self.start_btn.pack(side = tk.LEFT)
        self.draw_sp()


    def get_id(self):
        value = self.entry.get()
        if len(value) > 8:
            messagebox.showinfo("Ошибка", "Размер ID больше 8 символов!")
            return  # Прерываем выполнение, если ID недействителен
        else:
            self.entry.delete(0, tk.END)
            self.numdisk_val = value  # Присоединяем значение, если проверка пройдена
            self.create_disk()
            self.draw_sp()  # Вызываем отрисовку шпинделей после создания дисков

    def draw_sp(self):
        self.canvas.delete('all')  # Очищаем холст перед отрисовкой
        sp_width = 10
        sp_height = 100
        splind_position = [100, 200, 300, 400, 500, 600, 700, 800]

        for i in range(8):
            x = splind_position[i]
            self.canvas.create_rectangle(x - sp_width / 2, 100, x + sp_width / 2, 400, fill='red')

            for j, disk in enumerate(self.splindes[i]):
                diametr = i * 10 + (j + 1)
                disk_width = diametr
                disk_height = 20
                disk_x1 = x - disk_width / 2
                disk_x2 = x + disk_width / 2
                disk_y = 400 - (j + 1) * disk_height
                self.canvas.create_rectangle(disk_x1, disk_y, disk_x2, disk_y + disk_height, fill=disk.color)

    def create_disk(self):
        self.splindes = [[] for _ in range(8)]  # Сброс шпинделей перед созданием новых дисков
        for x, count_char in enumerate(self.numdisk_val):
            count = int(count_char)  # Преобразуем строку в число
            for _ in range(count):  # Создаем нужное количество дисков для каждого шпинделя
                disk = Disk(size=x)  # Создание диска с размером
                self.splindes[x].append(disk)  # Добавление диска в шпиндель

app = Tower(root)
root.mainloop()



'''
def get_id(self):
        value = self.entry.get()
        if len(value) > 8:
            messagebox.showinfo("Ошибка", "Размер ID больше 8 символов!")
            return  # Прерываем выполнение, если ID недействителен
        else:
            self.entry.delete(0, tk.END)
            self.numdisk_val = value  # Присоединяем значение, если проверка пройдена
            self.create_disk()
            self.draw_sp()  # Вызываем отрисовку шпинделей после создания дисков

    def draw_sp(self):
        self.canvas.delete('all')  # Очищаем холст перед отрисовкой
        sp_width = 10
        sp_height = 100
        splind_position = [100, 200, 300, 400, 500, 600, 700, 800]

        for i in range(8):
            x = splind_position[i]
            self.canvas.create_rectangle(x - sp_width / 2, 100, x + sp_width / 2, 400, fill='red')

            for j, disk in enumerate(self.splindes[i]):
                diametr = i * 10 + (j + 1)
                disk_width = diametr
                disk_height = 20
                disk_x1 = x - disk_width / 2
                disk_x2 = x + disk_width / 2
                disk_y = 400 - (j + 1) * disk_height
                self.canvas.create_rectangle(disk_x1, disk_y, disk_x2, disk_y + disk_height, fill=disk.color)

    def create_disk(self):
        self.splindes = [[] for _ in range(8)]  # Сброс шпинделей перед созданием новых дисков
        for x, count_char in enumerate(self.numdisk_val):
            count = int(count_char)  # Преобразуем строку в число
            for _ in range(count):  # Создаем нужное количество дисков для каждого шпинделя
                disk = Disk(size=x + 1)  # Создание диска с размером
                self.splindes[x].append(disk)  # Добавление диска в шпиндель'''