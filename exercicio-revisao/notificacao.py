from abc import ABC, abstractmethod
from functools import wraps

# Um decorator permite adicionar um comportamento antes e depois de um método
# sem repetir esse código em cada classe que realiza o envio.
def registrar_envio(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Iniciando envio da notificação")
        response = func(*args, **kwargs)
        print("Envio finalizado")
        return response
    return wrapper


# ABC indica que esta é uma classe base abstrata: ela define um contrato
# comum, mas não deve ser usada diretamente para criar objetos.
class Notificacao(ABC):

    def __init__(self, destinatario, mensagem):
        self.mensagem = mensagem
        self.destinatario = destinatario

    def exibir_dados(self):
        return self.destinatario, self.mensagem

    # Toda subclasse precisa fornecer sua própria forma de enviar.
    @abstractmethod
    def enviar(self):
        pass


# A classe herda os atributos e métodos comuns de Notificacao.
class NotificacaoEmail(Notificacao):

    def __init__(self, destinatario, mensagem):
        # super() chama o construtor da classe mãe e evita duplicação.
        super().__init__(destinatario, mensagem)

    # O decorator adiciona o registro do envio ao método de e-mail.
    @registrar_envio
    def enviar(self):
        # return devolve o resultado; quem chama o método decide como usá-lo.
        return f'E-mail enviado para {self.destinatario}'

class NotificacaoSMS(Notificacao):

    def __init__(self, destinatario, mensagem):
        super().__init__(destinatario, mensagem)

    # O mesmo contrato pode ter uma implementação diferente para SMS.
    @registrar_envio
    def enviar(self):
        return f'SMS enviado para {self.destinatario}'
        

if __name__ == '__main__':
    print(30 * '-')
    notificacao_email = NotificacaoEmail('Gabriel', 'Olá, tudo bem?')
    print(notificacao_email.exibir_dados())
    print(notificacao_email.enviar())
    print(30 * '-')
    notificacao_sms = NotificacaoSMS('Gabriel', 'Olá, tudo bem?')
    print(notificacao_sms.exibir_dados())
    print(notificacao_sms.enviar())
    print(30 * '-')