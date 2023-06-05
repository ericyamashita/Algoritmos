import tkinter as tk
import pyautogui

def atualizar_posicao():
    x, y = pyautogui.position()
    entry_posicao.delete(0, tk.END)
    entry_posicao.insert(0, f'X: {x} Y: {y}')
    root.after(100, atualizar_posicao)

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

label_num1 = tk.Label(root, text="posicao x:")
label_num1.pack()

entry_posicao_x = tk.Entry(root)
entry_posicao_x.pack()

label_num2 = tk.Label(root, text="Posicao y:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

label_num3 = tk.Label(root, text="Posicao x e y:")
label_num3.pack()

entry_posicao = tk.Entry(root)
entry_posicao.pack()
atualizar_posicao()


root.mainloop()