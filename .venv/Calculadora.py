import tkinter as tk
from tkinter import messagebox


def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    else:
        return x / y


def calcular():
    try:
        resultado = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(resultado))
    except Exception as e:
        messagebox.showerror("Erro", "Entrada inválida")


def adicionar_texto(texto):
    entry.insert(tk.END, texto)


def limpar():
    entry.delete(0, tk.END)


def sair():
    root.destroy()


root = tk.Tk()
root.title("Calculadora Digital")
root.configure(bg='black')

entry = tk.Entry(root, width=18, font=('Arial', 24), bd=8, insertwidth=2, bg="white", justify='right')
entry.grid(row=0, column=0, columnspan=4)

botoes = [
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('.', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('+', 3, 3),
    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('-', 4, 3),
    ('*', 5, 0), ('0', 5, 1), ('/', 5, 2), ('=', 5, 3)
]

for (texto, linha, coluna) in botoes:
    if texto == '=':
        botao = tk.Button(root, text=texto, padx=20, pady=20, font=('Arial', 18), bg="light blue", command=calcular)
    else:
        botao = tk.Button(root, text=texto, padx=20, pady=20, font=('Arial', 18), bg="light gray", command=lambda t=texto: adicionar_texto(t))
    botao.grid(row=linha, column=coluna, sticky="nsew")

botao_limpar = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), bg="gray", command=limpar)
botao_limpar.grid(row=1, column=2, sticky="nsew")

botao_sair = tk.Button(root, text='Sair', padx=20, pady=20, font=('Arial', 18), bg="red", command=sair)
botao_sair.grid(row=1, column=3, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
