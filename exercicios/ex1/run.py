from abc import ABC, abstractmethod



class Pagamento(ABC):
    def __init__(self, valor):
        self.valor = valor
       
    def exibir_valor(self):
        print(f"Valor do pagamento: {self.valor}")

    @abstractmethod 
    def processar_pagamento(self):
        pass

class PagamentoPix(Pagamento):
    def processar_pagamento(self):
        print(f"Processando pagamento via Pix no valor de {self.valor}.")

class PagamentoCartao(Pagamento):
    def __init__(self, valor, numero_cartao):
        super().__init__(valor)
        self.numero_cartao = numero_cartao

    def processar_pagamento(self):
        print(f"Processando pagamento via Cartão no valor de {self.valor}.")
        

pagamento_pix = PagamentoPix(100.0)
pagamento_pix.exibir_valor()
pagamento_cartao = PagamentoCartao(200.0, "1234-5678-9012-3456")
pagamento_cartao.exibir_valor()

# não vai funcionar, pois a classe Pagamento é abstrata e não pode ser instanciada diretamente
# pagamento_base = Pagamento(50.0)