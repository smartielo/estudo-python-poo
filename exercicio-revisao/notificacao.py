from abc import ABC, abstractmethod

def registrar_envio(func):
    def wrapper(*args, **kwargs):
        print("Iniciando envio da notificação") #mensagem antes de executar a função
        response = func(*args, **kwargs) #executando a função
        print("Envio finalizado") #mensagem após executar a função
        return response
    return wrapper


class Notificacao(ABC):

    def __init__(self, destinatario, mensagem):
        self.mensagem = mensagem
        self.destinatario = destinatario

    def exibir_dados(self):
        print(f'Mensagem: ', self.mensagem, 'Destinatario: ', self.destinatario)

    @abstractmethod
    def enviar(self, destinatario, mensagem):
        pass


class NotificacaoEmail(Notificacao):

    def __init__(self, destinatario, mensagem):
        super().__init__(destinatario, mensagem)

    @registrar_envio
    def enviar(self):
        print(f'Email Enviado para o destinatario: ', self.destinatario)

class NotificacaoSMS(Notificacao):

    def __init__(self, destinatario, mensagem):
        super().__init__(destinatario, mensagem)

    @registrar_envio
    def enviar(self):
        print(f'SMS Enviado para o destinatario: ', self.destinatario)


notificacao_email = NotificacaoEmail('Gabriel', 'Olá, tudo bem?')
notificacao_email.exibir_dados()
notificacao_email.enviar()

notificacao_sms = NotificacaoSMS('Gabriel', 'Olá, tudo bem?')
notificacao_sms.exibir_dados()
notificacao_sms.enviar()