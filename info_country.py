import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os
import requests
from io import BytesIO


paises = [
    {"nome": "Brasil", "bandeira": "https://flagcdn.com/w320/br.png", "info": "Capital: Brasília\nPopulação: 213 milhões"},
    {"nome": "França", "bandeira": "https://flagcdn.com/w320/fr.png", "info": "Capital: Paris\nPopulação: 67 milhões"},
    {"nome": "Japão", "bandeira": "https://flagcdn.com/w320/jp.png", "info": "Capital: Tóquio\nPopulação: 125 milhões"},
    {"nome": "Alemanha", "bandeira": "https://flagcdn.com/w320/de.png", "info": "Capital: Berlim\nPopulação: 83 milhões"},
    {"nome": "Canadá", "bandeira": "https://flagcdn.com/w320/ca.png", "info": "Capital: Ottawa\nPopulação: 38 milhões"},
    {"nome": "Austrália", "bandeira": "https://flagcdn.com/w320/au.png", "info": "Capital: Canberra\nPopulação: 26 milhões"},
    {"nome": "Argentina", "bandeira": "https://flagcdn.com/w320/ar.png", "info": "Capital: Buenos Aires\nPopulação: 45 milhões"},
    {"nome": "China", "bandeira": "https://flagcdn.com/w320/cn.png", "info": "Capital: Pequim\nPopulação: 1,4 bilhão"},
    {"nome": "Estados Unidos", "bandeira": "https://flagcdn.com/w320/us.png", "info": "Capital: Washington, D.C.\nPopulação: 331 milhões"},
    {"nome": "Itália", "bandeira": "https://flagcdn.com/w320/it.png", "info": "Capital: Roma\nPopulação: 60 milhões"},
    {"nome": "Índia", "bandeira": "https://flagcdn.com/w320/in.png", "info": "Capital: Nova Délhi\nPopulação: 1,4 bilhão"},
    {"nome": "Reino Unido", "bandeira": "https://flagcdn.com/w320/gb.png", "info": "Capital: Londres\nPopulação: 67 milhões"},
    {"nome": "México", "bandeira": "https://flagcdn.com/w320/mx.png", "info": "Capital: Cidade do México\nPopulação: 126 milhões"},
    {"nome": "Rússia", "bandeira": "https://flagcdn.com/w320/ru.png", "info": "Capital: Moscou\nPopulação: 144 milhões"},
    {"nome": "Espanha", "bandeira": "https://flagcdn.com/w320/es.png", "info": "Capital: Madri\nPopulação: 47 milhões"},
    {"nome": "Egito", "bandeira": "https://flagcdn.com/w320/eg.png", "info": "Capital: Cairo\nPopulação: 104 milhões"},
    {"nome": "África do Sul", "bandeira": "https://flagcdn.com/w320/za.png", "info": "Capital: Pretória\nPopulação: 60 milhões"},
    {"nome": "Coreia do Sul", "bandeira": "https://flagcdn.com/w320/kr.png", "info": "Capital: Seul\nPopulação: 52 milhões"},
    {"nome": "Portugal", "bandeira": "https://flagcdn.com/w320/pt.png", "info": "Capital: Lisboa\nPopulação: 10 milhões"},
    {"nome": "Turquia", "bandeira": "https://flagcdn.com/w320/tr.png", "info": "Capital: Ancara\nPopulação: 85 milhões"},
    {"nome": "Indonésia", "bandeira": "https://flagcdn.com/w320/id.png", "info": "Capital: Jacarta\nPopulação: 273 milhões"},
    {"nome": "Nigéria", "bandeira": "https://flagcdn.com/w320/ng.png", "info": "Capital: Abuja\nPopulação: 213 milhões"},
    {"nome": "Suécia", "bandeira": "https://flagcdn.com/w320/se.png", "info": "Capital: Estocolmo\nPopulação: 10 milhões"},
]

pontuacao_maxima = 0

class InfoCountryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("InfoCountry")
        self.pontuacao = 0
        self.pergunta_atual = 0
        self.paises_embaralhados = []

        self.tela_inicial()

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def tela_inicial(self):
        self.limpar_tela()
        tk.Label(self.root, text="🌎 InfoCountry", font=("Helvetica", 24, "bold")).pack(pady=20)
        tk.Label(self.root, text=f"🏆 Maior pontuação: {pontuacao_maxima}", font=("Helvetica", 16)).pack(pady=10)

        tk.Button(self.root, text="▶️ Jogar", font=("Helvetica", 14), command=self.iniciar_quiz).pack(pady=10)
        tk.Button(self.root, text="ℹ️ Informações dos Países", font=("Helvetica", 14), command=self.mostrar_infos).pack(pady=5)

    def iniciar_quiz(self):
        self.pontuacao = 0
        self.pergunta_atual = 0
        self.paises_embaralhados = random.sample(paises, len(paises))
        self.mostrar_pergunta()

    def mostrar_pergunta(self):
        self.limpar_tela()
        if self.pergunta_atual >= len(self.paises_embaralhados):
            self.mostrar_resultado()
            return

        pais = self.paises_embaralhados[self.pergunta_atual]
        response = requests.get(pais["bandeira"])
        img = Image.open(BytesIO(response.content))
        img = img.resize((300, 200))
        self.bandeira_img = ImageTk.PhotoImage(img)

        tk.Label(self.root, image=self.bandeira_img).pack(pady=20)
        tk.Label(self.root, text="De qual país é esta bandeira?", font=("Helvetica", 16)).pack(pady=10)

        self.resposta = tk.Entry(self.root, font=("Helvetica", 14))
        self.resposta.pack(pady=5)

        tk.Button(self.root, text="Responder", font=("Helvetica", 14), command=self.verificar_resposta).pack(pady=10)

    def verificar_resposta(self):
        resposta = self.resposta.get().strip().lower().upper()
        pais_correto = self.paises_embaralhados[self.pergunta_atual]["nome"].lower().upper()

        if resposta == pais_correto:
            self.pontuacao += 1

        self.pergunta_atual += 1
        self.mostrar_pergunta()

    def mostrar_resultado(self):
        global pontuacao_maxima
        if self.pontuacao > pontuacao_maxima:
            pontuacao_maxima = self.pontuacao

        self.limpar_tela()
        tk.Label(self.root, text=f"Você acertou {self.pontuacao} de {len(paises)}!", font=("Helvetica", 18)).pack(pady=20)
        tk.Button(self.root, text="Voltar ao Início", font=("Helvetica", 14), command=self.tela_inicial).pack(pady=10)

    def mostrar_infos(self):
        self.limpar_tela()
        tk.Label(self.root, text="📘 Informações dos Países", font=("Helvetica", 18)).pack(pady=10)
        for pais in paises:
            info = f"🌍 {pais['nome']}\n{pais['info']}\n"
            tk.Label(self.root, text=info, font=("Helvetica", 12), justify="left").pack(pady=5)
        tk.Button(self.root, text="⬅️ Voltar", font=("Helvetica", 14), command=self.tela_inicial).pack(pady=10)
      


if __name__ == "__main__":
   
    if not os.path.exists("bandeiras"):
        os.makedirs("bandeiras")
        print("⚠️ Adicione as imagens de bandeiras em 'bandeiras/' com nomes: brasil.png, franca.png, japao.png")
try:
    root = tk.Tk()
    app = InfoCountryApp(root)
    root.geometry("600x500")
    root.mainloop()
except Exception as e:
    print(f"Erro inesperado: {e}")

    root = tk.Tk()
    app = InfoCountryApp(root)
    root.geometry("500x500")
    root.mainloop()
