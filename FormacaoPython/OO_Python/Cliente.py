class Cliente:

    def __init__(self, nome):
        self.nome = nome

    @property
    def get_nome(self):
        print("Chamando @property nome()")
        return nome.title()

    @nome.setter
    def nome(self, nome):
        print("Chamando setter nome()")
        self.__nome = nome
