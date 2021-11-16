class Pessoa:
    def __init__(self, *filhos, nome=None, idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    marcelo = Pessoa(nome='marcelo')
    camila = Pessoa(marcelo, nome='camila')
    print(Pessoa.cumprimentar(camila))
    print(id(camila))
    print(camila.cumprimentar())
    print(camila.nome)
    print(camila.idade)
    for filho in camila.filhos:
        print(filho.nome)
    camila.sobrenome = 'lima'
    del camila.filhos
    print(camila.__dict__)
    print(marcelo.__dict__)
