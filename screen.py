import tkinter as tk
from random import choice, randint



class Screen:
    def __init__(self) -> None:
        self.screen = tk.Tk()

    def configureWindow(self) -> None:
        self.screen.iconbitmap("img/ico.ico")
        self.screen.title("Caça-Palavras")
        self.screen.resizable(False, False)
        self.screen.configure(bg="#BEB6E0")
        x = self.screen.winfo_screenwidth() // 2 - 400
        y = self.screen.winfo_screenheight() // 11
        self.screen.geometry(f"800x600+{x}+{y}")

    def closeWindow(self) -> None:
        self.screen.destroy()

    def cleanWindow(self) -> None:
        for componente in self.screen.winfo_children():
            componente.destroy()


class Draw:
    def __init__(self, screen: tk.Tk) -> None:
        self.screen = screen
        self.componentes = []
        self.palavrasCorretas = []
        self.imagens = []
        self.componentesSelecionados = []


    def drawLabel(self, text, posX, posY, tam=24) -> None:
        label = tk.Label(
            self.screen,
            text=text,
            font=("Arial", tam, "bold"),
            bg="#0000b7",
            fg="#ffffff",
            justify="center",
        )
        label.place(x=posX, y=posY)

    def drawButton(self, text, posX, posY, tam=12, comand=None) -> None:
        bt = tk.Button(
            self.screen,
            text=text,
            font=("Arial", tam, "bold"),
            bg="#000099",
            fg="#ffffff",
            borderwidth=4,
            relief="solid",
            width=12,
            height=1,
            command=comand,
        )
        bt.place(x=posX, y=posY)

    def drawBoard(self) -> None:
        widgets = [
            tk.Frame(self.screen, bg="#00005f", width=800, height=600),
            tk.Label(
                self.screen,
                text="Palavras:",
                font=("Arial", 19, "bold"),
                bg="#00005f",
                fg="#ffffff",
                justify="center",
            ),
        ]
        pos = [(0, 0), (14, 60)]
        x, y, i = 0, 1, 0
        for widget in widgets:
            widget.place(x=pos[i][x], y=pos[i][y])
            i += 1
        letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        tabuleiroPreenchido = 0
        x, y = 148, -1
        while not (tabuleiroPreenchido == 100):
            botao = tk.Button(
                self.screen,
                text=choice(letras),
                font=("Arial", 16, "bold"),
                width=4,
                height=2,
                bg="#BEB6E0",
                fg="#000000",
                borderwidth=4,
                relief="flat",
                command=lambda tab=tabuleiroPreenchido: click(self,
                    self.componentes[tab],
                    self.componentesSelecionados,
                ),
            )
            botao.place(x=x, y=y)
            self.componentes.append(botao)
            x += 65
            tabuleiroPreenchido += 1
            if tabuleiroPreenchido % 10 == 0:
                x = 148
                y += 59

    def drawWords(self, palavras: list) -> None:
        y = 15
        for palavra in palavras:
            tk.Label(
                self.screen,
                text=palavra,
                font=("Arial", 12, "bold"),
                bg="#00005f",
                fg="#ffffff",
                justify="center",
            ).place(x=19, y=150 + y)
            y += 45

        posPalavras = 0
        i = 0

        def posicionarPalavra(dir):
            nonlocal i, posPalavras
            posX = 0
            posY = 0
            if dir == 1:
                posX = randint(0, (9 - len(palavras[posPalavras]) + 1))
                posY = randint(0, 9)
            elif dir == 2:
                posX = randint(0, 9)
                posY = randint(0, (9 - len(palavras[posPalavras]) + 1))
            else:
                posX = randint(0, (9 - len(palavras[posPalavras]) + 1))
                posY = randint(0, (9 - len(palavras[posPalavras]) + 1))
            btPalavra = []
            if dir == 1:
                for x in range(posX, posX + len(palavras[posPalavras])):
                    btPos = (posY * 10) + x
                    for palavraCorreta in self.palavrasCorretas:
                        if self.componentes[btPos] in palavraCorreta:
                            i -= 1
                            return
            elif dir == 2:
                for y in range(posY, posY + len(palavras[posPalavras])):
                    btPos = (y * 10) + posX
                    for palavraCorreta in self.palavrasCorretas:
                        if self.componentes[btPos] in palavraCorreta:
                            i -= 1
                            return
            else:
                for y in range(posY, posY + len(palavras[posPalavras])):
                    btPos = (y * 10) + posX + (y - posY)
                    for palavraCorreta in self.palavrasCorretas:
                        if self.componentes[btPos] in palavraCorreta:
                            i -= 1
                            return

            btPos = (posY * 10) + posX
            for caractere in palavras[posPalavras]:
                self.componentes[btPos]["text"] = caractere
                btPalavra.append(self.componentes[btPos])

                if dir == 1:
                    btPos += 1
                elif dir == 2:
                    btPos += 10
                else:
                    btPos += 11
            self.palavrasCorretas.append(btPalavra)
            posPalavras += 1

        while i < len(palavras):
            posicionarPalavra(randint(1, 3))
            i += 1
            

    def drawFunc(self, janela: Screen, play) -> None:
        self.imagens.append(tk.PhotoImage(file="img/voltar.png"))
        btVoltar = tk.Button(
            self.screen,
            image=self.imagens[0],
            width=32,
            height=32,
            bg="#009BEE",
            borderwidth=2,
            relief="solid",
            command=lambda: voltarInicio(janela, self, play),
        )
        btVoltar.place(x=0, y=565)

    def restartDraw(self) -> None:
        self.componentes.clear()
        self.palavrasCorretas.clear()
        self.imagens.clear()


def voltarInicio(janela: Screen, desenho: Draw, inicio):
    janela.cleanWindow()
    desenho.restartDraw()
    inicio()


def click(self, botao: tk.Button, compSelecionados: list):
    if botao["bg"] == "#BEB6E0":
        botao["bg"] = "#052F23"
        compSelecionados.append(botao)
        if verificarPalavra(self, self.palavrasCorretas, self.componentesSelecionados):
            compSelecionados.clear()
            ...
    else:
        botao["bg"] = "#BEB6E0"
        compSelecionados.remove(botao)


def verificarPalavra(self, palavras: list, compSelecionados):
    y = 165
    acertou = False
    for palavra in palavras:
        if set(palavra) == set(compSelecionados):
            linha = tk.Frame(self.screen, bg='red', height=2, width=100)
            linha.place(x=10, y=y+10)
            acertou = True
            for comp in compSelecionados:
               comp["bg"] = "#BEB6E0"
               comp["fg"] = "#13A913"
            break
        y += 45
    return acertou
