from screen import Screen, Draw
import dataBase as dt


def play(janela, desenho) -> None:
    palavras = dt.loadWords()
    janela.cleanWindow()
    desenho.drawBoard()
    desenho.drawWords(palavras)
    desenho.drawFunc(main)


# ------------------------
def main() -> None:
    if janela.quantJanelas == 0:
        janela.configureWindow()
    desenho.drawLabel("CAÇA-PALAVRAS", 260, 85)
    desenho.drawButton("Jogar", 305, 245, 18, comand=lambda: play(janela, desenho))
    desenho.drawButton("Sair", 305, 320, 18, comand=janela.closeWindow)


if __name__ == "__main__":
    # Objetos
    janela = Screen()
    desenho = Draw(janela)
    # ------------------------
    main()
    # ------------------------
    janela.screen.mainloop()
