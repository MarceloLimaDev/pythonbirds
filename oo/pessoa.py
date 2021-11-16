class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    camila = Pessoa(nome='camila')
    marcelo = Pessoa(camila, nome='marcelo')
    print(Pessoa.cumprimentar(marcelo))
    print(id(marcelo))
    print(marcelo.cumprimentar())
    print(marcelo.nome)
    print(marcelo.idade)
    for filho in marcelo.filhos:
        print(filho.nome)
    marcelo.sobrenome = 'lima'
    del marcelo.filhos
    camila.olhos = 1
    del camila.olhos
    print(marcelo.__dict__)
    print(camila.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(marcelo.olhos)
    print(camila.olhos)
    print(id(Pessoa.olhos), id(marcelo.olhos), id(camila.olhos))