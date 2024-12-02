from abc import ABC, abstractmethod


class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass
        
    @abstractmethod
    def desligar(self):
        pass
        


class ControleTV(ControleRemoto):
    
    def ligar(self):
        return f'Ligando a TV...'
    
    def desligar(self):
        return f'Desligando a TV...'


class ControleArCondicionado(ControleRemoto):

    def ligar(self):
        print(f'Ligando o Ar Condicionado...')
    
    def desligar(self):
        print(f'Desligando o Ar Condicionado...')


controle = ControleTV()
print(controle.ligar())
print(controle.desligar())
print('=' * 40)#################################################
controle_ar = ControleArCondicionado()
controle_ar.ligar()