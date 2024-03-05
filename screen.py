from tkinter import Tk, Label, PhotoImage, Frame, Button, messagebox
from random import choice, randint


class Screen:

    def __init__(self) -> None:
        self.screen = Tk()

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


class Utility:

    def __init__(self, desenho, janela) -> None:
        self.quantAcertos = 0
        self.desenho = desenho
        self.janela = janela

    def voltarInicio(self, func, *param):
        self.janela.cleanWindow()
        self.desenho.restartDraw()
        if param == ():
            func()
        else:
            func(param[0], param[1])

    def click(self, botao: Button, main, play):
        if botao["bg"] == "#BEB6E0":
            botao["bg"] = "#052F23"
            self.desenho.componentesSelecionados.append(botao)
            if self.verificarPalavra(main, play):
                self.desenho.componentesSelecionados.clear()
        else:
            botao["bg"] = "#BEB6E0"
            self.desenho.componentesSelecionados.remove(botao)

    def verificarPalavra(self, main, play):
        y = 165
        acertou = False
        for palavra in self.desenho.palavrasCorretas:
            if set(palavra) == set(self.desenho.componentesSelecionados):
                linha = Frame(self.janela.screen, bg="red", height=2, width=98)
                linha.place(x=10, y=y + 11)
                acertou = True
                for comp in self.desenho.componentesSelecionados:
                    comp["bg"] = "#BEB6E0"
                    comp["fg"] = "#13A913"
                self.quantAcertos += 1
                if self.quantAcertos == 5:
                    self.quantAcertos = 0
                    res = messagebox.askyesno(
                        "Parabéns, você ganhou!",
                        "Deseja jogar novamente?",
                    )
                    if res:
                        self.voltarInicio(play, self.janela, self.desenho)
                    else:
                        self.voltarInicio(main)

                break
            y += 45
        return acertou


class Draw(Utility):

    def __init__(self, screen: Screen) -> None:
        super().__init__(self, screen)
        self.janela = screen
        self.componentes = []
        self.palavrasCorretas = []
        self.componentesSelecionados = []
        self.imagens = []

    def drawLabel(self, text, posX, posY, tam=24) -> None:
        label = Label(
            self.janela.screen,
            text=text,
            font=("Arial", tam, "bold"),
            bg="#BEB6E0",
            fg="#000000",
            justify="center",
        )
        label.place(x=posX, y=posY)

    def drawButton(self, text, posX, posY, tam=12, comand=None) -> None:
        bt = Button(
            self.janela.screen,
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

    def drawBoard(self, main, play) -> None:
        widgets = [
            Frame(self.janela.screen, bg="#00005f", width=800, height=600),
            Label(
                self.janela.screen,
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
            botao = Button(
                self.janela.screen,
                text=choice(letras),
                font=("Arial", 16, "bold"),
                width=4,
                height=2,
                bg="#BEB6E0",
                fg="#000000",
                borderwidth=4,
                relief="flat",
                command=lambda tab=tabuleiroPreenchido: self.click(
                    self.componentes[tab],
                    main,
                    play,
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
            Label(
                self.janela.screen,
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

            btPos = (posY * 10) + posX

            for caractere in palavras[posPalavras]:
                for index in range(len(palavras[posPalavras])):
                    pos = 0
                    if dir == 1:
                        pos = (posY * 10) + posX + index
                    elif dir == 2:
                        pos = ((posY + index) * 10) + posX
                    else:
                        pos = ((posY + index) * 10) + posX + index
                    for palavraCorreta in self.palavrasCorretas:
                        if self.componentes[pos] in palavraCorreta:
                            if self.componentes[pos]["text"] == caractere:
                                break
                            else:
                                i -= 1
                                return

                if self.componentes[btPos] not in btPalavra:
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

    def drawFunc(self, main) -> None:
        self.imagens.append(PhotoImage(file="img/voltar.png"))
        btVoltar = Button(
            self.janela.screen,
            image=self.imagens[0],
            bg="#009BEE",
            borderwidth=2,
            relief="solid",
            command=lambda: self.voltarInicio(main),
        )
        btVoltar.place(x=0, y=565)

    def restartDraw(self) -> None:
        self.componentes.clear()
        self.palavrasCorretas.clear()
        self.imagens.clear()


class Animation:
    def __init__(self, janela):
        self.janela = janela
