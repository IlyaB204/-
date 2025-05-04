import tkinter as tk
from tkinter import *
import math

from django.contrib.sitemaps.views import index

root = tk.Tk()
root.geometry('400x500')
root.title('Калькулятор')

def menu():
    pass

def add_digit(digit):
    value = entry.get()
    if value == '0':
        entry.delete(0, tk.END)
        entry.insert(0, digit)
    else:
        new_digit = entry.get()+ str(digit)
        entry.delete(0,tk.END)
        entry.insert(0,new_digit)

def add_operation(operation):
    value = entry.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    entry.delete(0, tk.END)
    entry.insert(0, value+operation)

def clear():
    entry.delete(0,tk.END)
    entry.insert(0, 0)

def calculate():
    try:
        value = entry.get()
        result = eval(value)
        add_history(f'{value} = {result}')
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        add_history(f'Ошибка {e}')
        entry.delete(0, tk.END)

def proc():
    value = entry.get()
    try:
        express = value.replace("%", "")
        result = eval(express)/100
        add_history(f'{value} = {result}')
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        add_history(f'Ошибка {e}')
        entry.delete(0, tk.END)

def pow_dig2():
    value = entry.get()
    result = int(value)**2
    add_history(f'{value} ^ 2 = {result}')
    entry.delete(0, tk.END)
    entry.insert(0, result)

def result_sqrt():
    try:
        value = entry.get()
        result = math.sqrt(int(value))
        add_history(f'{result}')
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        add_history(f'Ошибка {e}')
        entry.delete(0, tk.END)

def sum_rec(val):
    if int(val) < 10:
        return val
    else:
        new_val = sum(int(digit) for digit in str(val))
        return sum_rec(new_val)

def rec():
    digit = entry2.get()
    res = sum_rec(digit)
    print(f'Количество строк - {res}')
    text_result.config(height=res)

def add_history(operation):
    text_result.config(state='normal')
    text_result.insert(tk.END,f'{operation}\n')
    text_result.config(state='disabled')


expression = tk.StringVar(value="0")
text_result = tk.Text(root, height=11, width=33,state='disabled', wrap='word')
entry = tk.Entry(root, justify=tk.RIGHT, textvariable=expression)
tk.Label(text='Введите ID студента').grid(row=8, column=0, padx=5, pady=5)
entry2 = tk.Entry(root)
tk.Button(text='C', command=clear, width=5).grid(row=2,column=3,padx=5,pady=5, sticky = 'wens')
tk.Button(text='Menu', command=menu).grid(row=2,column=0,padx=5,pady=5, sticky = 'wens')
tk.Button(text='<>', command=rec).grid(row=2,column=1,padx=5,pady=5, sticky = 'wens')
tk.Button(text='=', command=calculate).grid(row=7, column=1,padx=5,pady=5,sticky ='wens', columnspan=2)
tk.Button(text="+", command = lambda :add_operation('+')).grid(row=4, column=3, padx=5, pady=5, sticky='wens')
tk.Button(text="%", command = lambda :proc()).grid(row=4, column=5, padx=5, pady=5, sticky='wens')
tk.Button(text="^2", command = lambda :pow_dig2()).grid(row=5, column=5, padx=5, pady=5, sticky='wens')
tk.Button(text="#", command = lambda :result_sqrt()).grid(row=5, column=5, padx=5, pady=5, sticky='wens')
tk.Button(text="-", command = lambda :add_operation('-')).grid(row=5, column=3, padx=5, pady=5, sticky='wens')
tk.Button(text="*", command = lambda :add_operation('*')).grid(row=6, column=3, padx=5, pady=5, sticky='wens')
tk.Button(text="/", command = lambda :add_operation('/')).grid(row=7, column=3, padx=5, pady=5, sticky='wens')
tk.Button(text='1', command=lambda: add_digit(1)).grid(row=4, column=0,padx=5,pady=5,sticky ='wens')
tk.Button(text='2', command=lambda: add_digit(2)).grid(row=4, column=1,sticky ='wens',padx=5,pady=5)
tk.Button(text='3', command=lambda: add_digit(3)).grid(row=4, column=2,padx=5,pady=5,sticky ='wens')
tk.Button(text='4', command=lambda: add_digit(4)).grid(row=5, column=0,padx=5,pady=5,sticky ='wens')
tk.Button(text='5', command=lambda: add_digit(5)).grid(row=5, column=1,padx=5,pady=5,sticky ='wens')
tk.Button(text='6', command=lambda: add_digit(6)).grid(row=5, column=2,padx=5,pady=5,sticky ='wens')
tk.Button(text='7', command=lambda: add_digit(7)).grid(row=6, column=0,padx=5,pady=5,sticky ='wens')
tk.Button(text='8', command=lambda: add_digit(8)).grid(row=6, column=1,padx=5,pady=5,sticky ='wens')
tk.Button(text='9', command=lambda: add_digit(9)).grid(row=6, column=2,padx=5,pady=5,sticky ='wens')
tk.Button(text='0', command=lambda: add_digit(0)).grid(row=7, column=0,padx=5,pady=5,sticky ='wens')
text_result.grid(row=0, column=0,padx=5,pady=5, sticky = 'wens',columnspan=3)
entry.grid(row = 1, column=0, padx=5,pady=5, sticky='wens', columnspan= 3)
entry2.grid(row=9, column=0,padx = 5, pady=5, columnspan=2)

root.mainloop()