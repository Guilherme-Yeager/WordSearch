import pandas as pd


def loadWords():
    dados = pd.read_csv("data/dados.csv").sample(n=5).to_dict()
    lista = []
    for _, v in dados['Palavras'].items():
        lista.append(v)
    return lista


if __name__ == "__main__":
    dic = {
        "Palavras": [
            "DIA",
            "CODIGO",
            "CASA",
            "NAVIO",
            "VASCO",
            "GATO",
            "DADO",
            "CADEIRA",
            "NUVEM",
            "REDE",
            "PAPEL",
            "OVO",
            "RATO",
            "ZEBRA",
        ]
    }

    dados = pd.DataFrame(dic)
    dados.to_csv("data/dados.csv", index=False)
