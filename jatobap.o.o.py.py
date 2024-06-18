# fazer a classe
class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo

    def acelerar(self):
        print("acelerando!")

    def frear(self):
        print("freando")
    
    #criando o objeto da classe. "instancia"
carro1 = Carro("Acelerando",100,)
carro2 = Carro("Freando",30,)

#chamando o objeto na tela 

print("meu carro está {} a {} kmh".format(carro1.acao,carro1.velocidade))
carro1.acelerar()

print("meu carro está {} a {} kmh".format(carro2.acao,carro2.velocidade))
carro2.frear()
