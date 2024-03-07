from dataBase import loadWords
from screen import Screen, Draw


def play(janela: Screen, desenho: Draw) -> None:
    palavras = loadWords()
    janela.cleanWindow()
    desenho.drawBoard(main, play)
    desenho.drawWords(palavras)
    desenho.drawFunc(main)

def main() -> None:
    desenho.drawBgMenu()
    desenho.drawLabel("CAÇA-PALAVRAS", 240, 90, tam=28)
    desenho.drawButton("Jogar", 328, 235, 18, comand=lambda: play(janela, desenho))
    desenho.drawButton("Sair", 328, 310, 18, comand=janela.closeWindow)

if __name__ == "__main__":
    janela = Screen()
    janela.configureWindow()
    desenho = Draw(janela)
    main()
    janela.screen.mainloop()
