from dataBase import loadWords
from screen import Screen, Draw, Animation


def play(janela: Screen, desenho: Draw) -> None:
    palavras = loadWords()
    janela.cleanWindow()
    desenho.drawBoard(main , play)
    desenho.drawWords(palavras)
    desenho.drawFunc(main)


def main() -> None:
    desenho.drawLabel("CAÇA-PALAVRAS", 260, 85)
    desenho.drawButton("Jogar", 305, 245, 18, comand=lambda: play(janela, desenho))
    desenho.drawButton("Sair", 305, 320, 18, comand=janela.closeWindow)


if __name__ == "__main__":
    # Objetos
    janela = Screen()
    janela.configureWindow()
    desenho = Draw(janela)
    animacao = Animation(janela)
    main()
    janela.screen.mainloop()
