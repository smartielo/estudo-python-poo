from notificacao import NotificacaoSMS, Notificacao, NotificacaoEmail
import pytest

def test_notificacao_sms():
    notificacao_sms = NotificacaoSMS(
        destinatario="Gabriel",
        mensagem="Hello World"
    )

    assert notificacao_sms.enviar() == "SMS Enviado para o destinatario: Gabriel"


def test_notificacao_email():
    notificacao_email = NotificacaoEmail(
        destinatario="Gabriel",
        mensagem="Hello World"
    )

    gba = notificacao_email.enviar()

    assert notificacao_email.enviar() == "Email Enviado para o destinatario: Gabriel"



def test_classe_abstrata():
    with pytest.raises(TypeError):
        Notificacao(
            destinatario="123456789",
            mensagem="Teste de notificação SMS"
        )  