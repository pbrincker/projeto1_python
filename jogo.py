
from random import randint


class Personagem():
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"

    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = self.__nivel * randint(2, 5)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano")   


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def ataque_especial(self, alvo):
        dano = self.get_nivel() * randint(5, 8)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()}, atacou {alvo.get_nome()} e causou {dano} de dano")

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"


class Vilao(Personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"


class Jogo:
    ''' Orquestrador do jogo '''
    def __init__(self) -> None:
        self.heroi = Heroi("Kakashi", 1000, 150, 'Raio')
        self.vilao = Vilao("Urubu", 2500, 60, 'Voador')

    def iniciar_batalha(self):
        ''' Fazer a gestão da batalha nos turnos '''
        print("Iniciando a batalha")
        while self.heroi.get_vida() > 0 and self.vilao.get_vida() > 0:
            print("\nDetalhes dos personagens: ")
            print(self.heroi.exibir_detalhes())
            print(self.vilao.exibir_detalhes())

            input("Pressione Enter para atacar....")

            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")

            if escolha == '1':
                self.heroi.atacar(self.vilao)
            elif escolha == '2':
                self.heroi.ataque_especial(self.vilao)
            else:
                print("Escolha outro valor")
            if self.vilao.get_vida() > 0:
                self.vilao.atacar(self.heroi)
        if self.heroi.get_vida() > 0:
            print('Parabéns, você venceu a batalha')
        else:
            print('Você foi derrotado!')


jogo = Jogo()
jogo.iniciar_batalha()
