import tkinter as tk

root = tk.Tk()
root.title("Jogo da Adivinhação")

largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

pos_x = (largura_tela - 450) // 2
pos_y = (altura_tela - 300) // 2

root.geometry("450x300+{}+{}".format(pos_x, pos_y))
root.resizable(False, False)

dica = tk.Label(root, text="Dica:", font=("Arial", 12))
ultima_tentativa = tk.Label(root, text="Última tentativa:", font=("Arial", 12))
tentativas = tk.Label(root, text="Tentativas:", font=("Arial", 12))
acertos = tk.Label(root, text="Acertos:", font=("Arial", 12))
entrada = tk.Entry(root, font=("Arial", 10))

botao = tk.Button(root, text="Enviar", font=("Arial", 10), width=10)
botao2 = tk.Button(root, text="Reiniciar", font=("Arial", 10), width=10)
botao3 = tk.Button(root, text="Dica especial", font=("Arial", 10), width=10)

dica.grid(row=0, column=1, pady=5, padx=10, sticky=tk.W)
ultima_tentativa.grid(row=1, column=1, pady=5, padx=10, sticky=tk.W)
tentativas.grid(row=2, column=1, pady=5, padx=10, sticky=tk.W)
acertos.grid(row=3, column=1, pady=5, padx=10, sticky=tk.W)
entrada.grid(row=4, column=1, pady=5, padx=10, sticky=tk.W)

tk.Label(root).grid(row=5, column=0, columnspan=3)

botao3.grid(row=6, column=0, pady=15, padx=(10, 5), sticky=tk.W)  
botao2.grid(row=6, column=1, pady=15, padx=5)  
botao.grid(row=6, column=2, pady=15, padx=(5, 10), sticky=tk.E) 

root.mainloop()