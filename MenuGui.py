import tkinter as tk
import pyautogui

def abrir_opcao1():
    print("Opção 1 selecionada")

def abrir_opcao2():
    print("Opção 2 selecionada")
  
def abrir_opcao3():
    print("Opção 3 selecionada")

def sair():
    root.destroy()

root = tk.Tk()
#nome no display
root.title("Menu")
#tamanho da tela do app
root.geometry("400x400")

menu = tk.Menu(root)
root.config(menu=menu)

opcoes_menu = tk.Menu(menu)
menu.add_cascade(label="Opções", menu=opcoes_menu)
opcoes_menu.add_command(label="Opção 1", command=abrir_opcao1)
opcoes_menu.add_command(label="Opção 2", command=abrir_opcao2)
opcoes_menu.add_command(label="Opção 3", command=abrir_opcao3)

opcoes_menu.add_separator()

opcoes_menu.add_command(label="Sair", command=sair)

label_num1 = tk.Label(root, text="Posicao 1:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Posicao 2:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()


root.mainloop()