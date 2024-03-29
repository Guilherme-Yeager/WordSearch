from tkinter import Tk, Label, PhotoImage, Frame, Button, messagebox, Toplevel
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
        self.quantAcertos = [0, 0, 0, 0, 0]
        self.desenho = desenho
        self.janela = janela

    def voltarInicio(self, func, vencedor=0):
        resp = None
        if vencedor == 0:
            resp = messagebox.askyesno(
                "Voltar",
                "Deseja voltar ao menu principal?",
            )
            if not resp:
                return

        self.janela.cleanWindow()
        self.desenho.restartDraw()
        if resp:
            func()
        elif vencedor == 1:
            func()
        else:
            func(self.janela, self.desenho)

    def click(self, botao: Button, main, play):
        if botao["bg"] == "#BEB6E0":
            botao["bg"] = "#052F23"
            self.desenho.componentesSelecionados.append(botao)
        else:
            botao["bg"] = "#BEB6E0"
            self.desenho.componentesSelecionados.remove(botao)
        if self.verificarPalavra(main, play):
            self.desenho.componentesSelecionados.clear()

    def verificarPalavra(self, main, play):
        y = 165
        acertou = False
        for i, palavra in enumerate(self.desenho.palavrasCorretas):
            if set(palavra) == set(self.desenho.componentesSelecionados):
                linha = Frame(self.janela.screen, bg="red", height=2, width=98)
                linha.place(x=10, y=y + 11)
                acertou = True
                for comp in self.desenho.componentesSelecionados:
                    comp["bg"] = "#BEB6E0"
                    comp["fg"] = "#13A913"
                self.quantAcertos[i] = 1
                if set(self.quantAcertos) == {1}:
                    self.quantAcertos = [0, 0, 0, 0, 0]
                    res = messagebox.askyesno(
                        "Parabéns, você ganhou!",
                        "Deseja jogar novamente?",
                    )
                    if res:
                        self.voltarInicio(
                            play,
                            vencedor=2,
                        )
                    else:
                        self.voltarInicio(
                            main,
                            vencedor=1,
                        )

                break
            y += 45
        return acertou

    def inverterPalavra(self, btPalavra):
        if randint(0, 1) == 1:
            listCaracter = []
            for bt in btPalavra:
                listCaracter.append(bt["text"])
                btPos = -1
            for bt in btPalavra:
                bt["text"] = listCaracter[btPos]
                btPos -= 1

    def configurarJogo(self):
        pass


class Draw(Utility):

    def __init__(self, screen: Screen) -> None:
        super().__init__(self, screen)
        self.janela = screen
        self.componentes = []
        self.palavrasCorretas = []
        self.componentesSelecionados = []
        self.imagens = []

    def drawBgMenu(self):
        self.imagens.append(PhotoImage(file="img/menu.png"))
        labelBg = Label(self.janela.screen, image=self.imagens[0])
        labelBg.place(x=-2, y=-2)

    def drawLabel(self, text, posX, posY, tam=20) -> None:
        label = Label(
            self.janela.screen,
            text=text,
            font=("Arial", tam, "bold"),
            bg="#0646AF",
            fg="#ffffff",
            justify="center",
            borderwidth=4,
            relief="raised",
        )
        label.place(x=posX, y=posY)

    def drawButton(self, text, posX, posY, tam=14, comand=None) -> None:
        bt = Button(
            self.janela.screen,
            text=text,
            font=("Arial", tam, "bold"),
            bg="#000099",
            fg="#ffffff",
            borderwidth=4,
            relief="solid",
            width=10,
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
            elif dir == 3:
                posX = randint(0, (9 - len(palavras[posPalavras]) + 1))
                posY = randint(0, (9 - len(palavras[posPalavras]) + 1))
            else:
                posX = randint(len(palavras[posPalavras]) - 1, 9)
                posY = randint(0, (9 - len(palavras[posPalavras]) + 1))
            btPalavraDepois = []
            btPalavraAntes = []

            btPos = (posY * 10) + posX
            conflito = False
            for caractere in palavras[posPalavras]:
                for palavraCorreta in self.palavrasCorretas:  # Colisão
                    if self.componentes[btPos] in palavraCorreta:
                        if self.componentes[btPos]["text"] == caractere:
                            conflito = True
                            break
                        else:
                            i -= 1
                            if btPalavraDepois != []:
                                for enum, c in enumerate(btPalavraAntes):
                                    btPalavraDepois[enum]["text"] = c
                            return

                btPalavraAntes.append(self.componentes[btPos]["text"])
                self.componentes[btPos]["text"] = caractere
                btPalavraDepois.append(self.componentes[btPos])

                if dir == 1:
                    btPos += 1
                elif dir == 2:
                    btPos += 10
                elif dir == 3:
                    btPos += 11
                else:
                    btPos += 9

            if not conflito:
                self.inverterPalavra(btPalavraDepois)
            self.palavrasCorretas.append(btPalavraDepois)
            posPalavras += 1

        while i < len(palavras):
            posicionarPalavra(randint(1, 4))
            i += 1

    def drawFunc(self, main) -> None:
        if self.imagens == []:
            self.imagens.append(None)
        self.imagens.append(PhotoImage(file="img/voltar.png"))
        btVoltar = Button(
            self.janela.screen,
            image=self.imagens[1],
            bg="#009BEE",
            borderwidth=2,
            relief="solid",
            command=lambda: self.voltarInicio(main),
        )
        btVoltar.place(x=0, y=565)
        self.imagens.append(PhotoImage(file="img/configurar.png"))
        btConfigurar = Button(
            self.janela.screen,
            image=self.imagens[2],
            bg="#009BEE",
            borderwidth=2,
            relief="solid",
            command=self.configurarJogo,
        )
        btConfigurar.place(x=110, y=565)

    def restartDraw(self) -> None:
        self.componentes.clear()
        self.palavrasCorretas.clear()
        self.imagens.clear()
