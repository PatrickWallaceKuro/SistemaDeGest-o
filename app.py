import customtkinter as ctk
from tkinter import *
import sqlite3
from tkinter import messagebox


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configuracoes_da_janela_inicial()
        self.primeira_pagina()

        #configurando a janela principal

    def configuracoes_da_janela_inicial(self):
        self.geometry("1000x500")
        self.title("Sistema de login")
        self.resizable(False, False)

    def primeira_pagina(self):
        #Criar frame dos botões
        self.frame_botoes = ctk.CTkFrame(self, width=400, height=50)
        self.frame_botoes.grid(row = 1, column = 0, padx = 10, pady = 40, sticky = "")

        #botão de cadastro
        self.btn_cadastro = ctk.CTkButton(self.frame_botoes, width=400, text="Cadastar Empresa".upper(), font=("Arial black", 12), fg_color="#3bac4e", hover_color="#116d20", command=self.tela_cadastro_empresa)
        self.btn_cadastro.grid(row=0, column=0, padx=10, pady=10)

        #botão de pedido
        self.btn_cadastro = ctk.CTkButton(self.frame_botoes, width=400, text="novo pedido".upper(), font=("Arial black", 12))
        self.btn_cadastro.grid(row=0, column=1, padx=10, pady=10)

        #Criar frame da tabela de ultimos pedidos
        self.frame_ultimo_pedido = ctk.CTkFrame(self, width = 800, height = 300)
        self.frame_ultimo_pedido.grid (row = 3 , column = 0, padx = 10, pady = 10, sticky ="")

    def tela_cadastro_empresa(self):
        #removendo a primeira pagina
        self.frame_botoes.grid_forget()
        self.frame_ultimo_pedido.grid_forget()

        #criando frame do cadastro
        self.frame_cadastro = ctk.CTkFrame(self, width=980, height=480)
        self.frame_cadastro.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "")

        #Criando campos de cadastro
        #nome empresa

        self.empresa_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, placeholder_text="EMPRESA", font=("Arial black", 16), border_color="#2596be", width = 300)
        self.empresa_cadastro_entry.grid(row=0, column=0, padx=10, pady=10, sticky = "ew")

        #cnpj empresa

        self.cnpj_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, placeholder_text="CNPJ", font=("Arial black", 16),border_color="#2596be", width = 300)
        self.cnpj_cadastro_entry.grid(row=0, column=1, padx=10, pady=10, sticky = "ew")
        self.cnpj_cadastro_entry.bind("<KeyRelease>", self.formatar_cnpj)
        
        #endereço 
        self.endereco_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, placeholder_text ="Endereço", font=("Arial black", 16), border_color="#2596be", width = 600)
        self.endereco_cadastro_entry.grid(row=1 , column = 0, columnspan=3, padx = 10, pady = 10, sticky = "ew")

        #informações adicionais 
        self.info_cadastrar_entry = ctk.CTkTextbox(self.frame_cadastro, font=("Arial black", 16), border_color="#2596be", width = 600, height = 300)
        self.info_cadastrar_entry.grid(row=2 , column = 0, columnspan=3, padx = 10, pady = 10, sticky = "ew")

        #botão cadastrar
        self.btn_cadastro_entry = ctk.CTkButton(self.frame_cadastro, width=400, text="cadastrar".upper(), font=("Arial black", 12))
        self.btn_cadastro_entry.grid(row=3, column=0, padx=10, pady=10)

        #botão voltar
        self.btn_voltar_entry = ctk.CTkButton(self.frame_cadastro, width=400, text="voltar".upper(), font=("Arial black", 12), command=self.voltar_primeira_pagina)
        self.btn_voltar_entry.grid(row=3, column=1, padx=10, pady=10)


    def voltar_primeira_pagina(self):
        #destruindo o frame de cadastro para voltar a pagina
        self.frame_cadastro.destroy()
        self.primeira_pagina()


    def formatar_cnpj(self, event=None):
        texto = self.cnpj_cadastro_entry.get()

        # remove tudo que não for número
        numeros = "".join(filter(str.isdigit, texto))

        # limita a 14 dígitos
        numeros = numeros[:14]

        # aplica a máscara
        cnpj_formatado = ""
        for i, char in enumerate(numeros):
            if i == 2 or i == 5:
                cnpj_formatado += "."
            elif i == 8:
                cnpj_formatado += "/"
            elif i == 12:
                cnpj_formatado += "-"
            cnpj_formatado += char

        # atualiza o entry
        self.cnpj_cadastro_entry.delete(0, "end")
        self.cnpj_cadastro_entry.insert(0, cnpj_formatado)
if __name__=="__main__":
    app = App()
    app.mainloop()