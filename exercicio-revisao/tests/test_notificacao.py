from notificacao import NotificacaoSMS, Notificacao, NotificacaoEmail
import pytest

def test_notificacao_sms():
    notificacao_sms = NotificacaoSMS(
        destinatario="Gabriel",
        mensagem="Hello World"
    )

    assert notificacao_sms.enviar() == "SMS enviado para Gabriel"


def test_notificacao_email():
    notificacao_email = NotificacaoEmail(
        destinatario="Gabriel",
        mensagem="Hello World"
    )

    assert notificacao_email.enviar() == "E-mail enviado para Gabriel"



def test_exibir_dados():
    notificacao_email = NotificacaoEmail(
        destinatario="Gabriel",
        mensagem="Hello World"
    )
    notificacao_sms = NotificacaoSMS(
        destinatario="Gabriel",
        mensagem="Hello World"
    )

    assert notificacao_email.exibir_dados() == ("Gabriel", "Hello World")
    assert notificacao_sms.exibir_dados() == ("Gabriel", "Hello World")


def test_classe_abstrata():
    with pytest.raises(TypeError):
        Notificacao(
            destinatario="Gabriel",
            mensagem="Hello World"
        )
