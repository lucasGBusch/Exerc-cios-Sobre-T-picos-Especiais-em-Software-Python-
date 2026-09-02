class Participante:
    def __init__(self, nome, idade, email, categoria, valor_pago):
        self.nome = nome
        self._idade = idade
        self.email = email
        self.categoria = categoria
        self.__valor_pago = valor_pago

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        self._idade = nova_idade

    @property
    def valor_pago(self):
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, nova_valor_pago):
        
        if nova_valor_pago >= 0:
            self.__valor_pago = nova_valor_pago
        else:
            print("Numero negativo...")

    def mostrar_dados(self):
            print("=====================")
            print(f"Nome       : {self.nome}")
            print(f"Idade      : {self.idade}")
            print(f"Email      : {self.email}")
            print(f"Categoria  : {self.categoria}")
            print(f"Valor Pago : {self.valor_pago}")
