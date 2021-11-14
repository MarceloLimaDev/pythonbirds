class Pessoa:
    def __init__(self, nome=None, idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    marcelo = Pessoa(nome='Marcelo')
    camila = Pessoa(marcelo, nome='Camila')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(camila.cumprimentar())
    print(camila.nome)
    print(camila.idade)
    for filho in camila.filhos:
        print(filho.nome)



