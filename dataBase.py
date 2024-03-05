from pandas import DataFrame, read_csv


def loadWords():
    dados = read_csv("data/dados.csv").sample(n=5).to_dict()
    lista = []
    for _, v in dados["Palavras"].items():
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
            "GALO",
            "VAGNER",
            "SAPO",
            "GREMIO",
            "ALCIDES",
            "RAPHAEL",
            "MAYLI",
            "JOSEVAL",
            "ANDRE",
            "ANDRES",
        ]
    }

    dados = DataFrame(dic)
    dados.to_csv("data/dados.csv", index=False)
