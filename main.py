import screen as screen
import dataBase as dt


def voltarInicio() -> None:
    desenho.drawLabel("CAÇA-PALAVRAS", 260, 85)
    desenho.drawButton("Jogar", 305, 245, 18, comand=lambda: play(janela, desenho))
    desenho.drawButton("Sair", 305, 320, 18, comand=janela.closeWindow)


def play(janela, desenho) -> None:
    palavras = dt.loadWords()
    janela.cleanWindow()
    desenho.drawBoard()
    desenho.drawWords(palavras)
    desenho.drawFunc(janela, voltarInicio)


# ------------------------
def main() -> None:
    janela.configureWindow()
    desenho.drawLabel("CAÇA-PALAVRAS", 260, 85)
    desenho.drawButton("Jogar", 305, 245, 18, comand=lambda: play(janela, desenho))
    desenho.drawButton("Sair", 305, 320, 18, comand=janela.closeWindow)


if __name__ == "__main__":
    # Objetos
    janela = screen.Screen()
    desenho = screen.Draw(janela.screen)
    # ------------------------
    main()
    # ------------------------
    janela.screen.mainloop()
