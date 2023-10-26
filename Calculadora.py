import tkinter as tk
from tkinter import Entry, Button

# Função para adicionar um caractere ao campo de entrada
def press(key):
    entry.insert(tk.END, key)

# Função para limpar o campo de entrada
def clear():
    entry.delete(0, tk.END)

# Função para calcular o resultado
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")

# Cria uma janela principal
root = tk.Tk()
root.title("Calculadora Transparente")
root.attributes('-alpha', 0.9)  # Define a transparência (0.0 a 1.0)
root.configure(bg='black')  # Define o plano de fundo para preto

# Cria um campo de entrada para a calculadora
entry = Entry(root, width=20, font=('Arial', 16), bg='black', fg='white')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row, col = 1, 0

# Cria os botões da calculadora com as funções apropriadas
for button_text in buttons:
    if button_text == '=':
        Button(root, text=button_text, command=calculate, height=2, width=5, bg='gray', fg='white').grid(row=row, column=col)
    elif button_text == 'C':
        Button(root, text=button_text, command=clear, height=2, width=5, bg='gray', fg='white').grid(row=row, column=col)
    else:
        Button(root, text=button_text, command=lambda key=button_text: press(key), height=2, width=5, bg='gray', fg='white').grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Inicia o loop principal do aplicativo
root.mainloop()
