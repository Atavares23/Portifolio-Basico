# Calculadora com interface gráfica usando tkinter
import tkinter as tk
from tkinter import messagebox
import math
import numpy as np

# Funções para operações matemáticas
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

def media(x, y):
    return (x + y) / 2

def raiz(x):
    return math.sqrt(x)

def progressao_aritmetica(inicio, razao, termos):
    return np.arange(inicio, inicio + razao * termos, razao)

# Função para processar a operação selecionada
def calcular():
    operacao = operacao_var.get()
    try:
        if operacao == "Raiz":
            num1 = float(entry1.get())
            resultado = raiz(num1)
            messagebox.showinfo("Resultado", f"A raiz quadrada de {num1} é {resultado}")
        elif operacao == "P.A":
            inicio = int(entry1.get())
            razao = int(entry2.get())
            termos = int(entry3.get())
            pa = progressao_aritmetica(inicio, razao, termos)
            soma = sum(pa)
            messagebox.showinfo("Resultado", f"A P.A é: {pa} e a soma é: {soma}")
        else:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            if operacao == "Adição":
                resultado = add(num1, num2)
            elif operacao == "Subtração":
                resultado = subtract(num1, num2)
            elif operacao == "Multiplicação":
                resultado = multiply(num1, num2)
            elif operacao == "Divisão":
                resultado = divide(num1, num2)
            elif operacao == "Média":
                resultado = media(num1, num2)
            messagebox.showinfo("Resultado", f"O resultado é: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora")

# Widgets
tk.Label(root, text="Número 1:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Número 2:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Número 3 (P.A):").grid(row=2, column=0, padx=10, pady=5)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Operação:").grid(row=3, column=0, padx=10, pady=5)
operacao_var = tk.StringVar(value="Adição")
tk.OptionMenu(root, operacao_var, *operacoes).grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Calcular", command=calcular).grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar o loop da interface gráfica
root.mainloop()