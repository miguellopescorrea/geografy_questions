import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os

paises = [
    {"nome": "Brasil", "bandeira": "bandeiras/brasil.png", "info": "Capital: Brasília\nPopulação: 213 milhões"},
    {"nome": "França", "bandeira": "bandeiras/franca.png", "info": "Capital: Paris\nPopulação: 67 milhões"},
    {"nome": "Japão", "bandeira": "bandeiras/japao.png", "info": "Capital: Tóquio\nPopulação: 125 milhões"},
    {"nome": "Alemanha", "bandeira": "bandeiras/alemanha.png", "info": "Capital: Berlim\nPopulação: 83 milhões"},
    {"nome": "Canadá", "bandeira": "bandeiras/canada.png", "info": "Capital: Ottawa\nPopulação: 38 milhões"},
    {"nome": "Austrália", "bandeira": "bandeiras/australia.png", "info": "Capital: Canberra\nPopulação: 26 milhões"},
    {"nome": "Argentina", "bandeira": "bandeiras/argentina.png", "info": "Capital: Buenos Aires\nPopulação: 45 milhões"},
    {"nome": "China", "bandeira": "bandeiras/china.png", "info": "Capital: Pequim\nPopulação: 1,4 bilhão"},
    {"nome": "Estados Unidos", "bandeira": "bandeiras/eua.png", "info": "Capital: Washington, D.C.\nPopulação: 331 milhões"},
    {"nome": "Itália", "bandeira": "bandeiras/italia.png", "info": "Capital: Roma\nPopulação: 60 milhões"},
    {"nome": "Índia", "bandeira": "bandeiras/india.png", "info": "Capital: Nova Délhi\nPopulação: 1,4 bilhão"},
    {"nome": "Reino Unido", "bandeira": "bandeiras/reino_unido.png", "info": "Capital: Londres\nPopulação: 67 milhões"},
    {"nome": "México", "bandeira": "bandeiras/mexico.png", "info": "Capital: Cidade do México\nPopulação: 126 milhões"},
    {"nome": "Rússia", "bandeira": "bandeiras/russia.png", "info": "Capital: Moscou\nPopulação: 144 milhões"},
    {"nome": "Espanha", "bandeira": "bandeiras/espanha.png", "info": "Capital: Madri\nPopulação: 47 milhões"},
    {"nome": "Egito", "bandeira": "bandeiras/egito.png", "info": "Capital: Cairo\nPopulação: 104 milhões"},
    {"nome": "África do Sul", "bandeira": "bandeiras/africa_do_sul.png", "info": "Capital: Pretória\nPopulação: 60 milhões"},
    {"nome": "Coreia do Sul", "bandeira": "bandeiras/coreia_do_sul.png", "info": "Capital: Seul\nPopulação: 52 milhões"},
    {"nome": "Portugal", "bandeira": "bandeiras/portugal.png", "info": "Capital: Lisboa\nPopulação: 10 milhões"},
    {"nome": "Turquia", "bandeira": "bandeiras/turquia.png", "info": "Capital: Ancara\nPopulação: 85 milhões"},
    {"nome": "Indonésia", "bandeira": "bandeiras/indonesia.png", "info": "Capital: Jacarta\nPopulação: 273 milhões"},
    {"nome": "Nigéria", "bandeira": "bandeiras/nigeria.png", "info": "Capital: Abuja\nPopulação: 213 milhões"},
    {"nome": "Suécia", "bandeira": "bandeiras/suecia.png", "info": "Capital: Estocolmo\nPopulação: 10 milhões"},
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
        img = Image.open(pais["bandeira"])
        img = img.resize((300, 200))
        self.bandeira_img = ImageTk.PhotoImage(img)

        tk.Label(self.root, image=self.bandeira_img).pack(pady=20)
        tk.Label(self.root, text="De qual país é esta bandeira?", font=("Helvetica", 16)).pack(pady=10)

        self.resposta = tk.Entry(self.root, font=("Helvetica", 14))
        self.resposta.pack(pady=5)

        tk.Button(self.root, text="Responder", font=("Helvetica", 14), command=self.verificar_resposta).pack(pady=10)

    def verificar_resposta(self):
        resposta = self.resposta.get().strip().lower()
        pais_correto = self.paises_embaralhados[self.pergunta_atual]["nome"].lower()

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

    root = tk.Tk()
    app = InfoCountryApp(root)
    root.geometry("500x500")
    root.mainloop()
