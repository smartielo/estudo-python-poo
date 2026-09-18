from notificacao import NotificacaoSMS
import pytest

def test_notificacao_sms():
    notificacao_sms = NotificacaoSMS(
        destinatario="123456789",
        mensagem="Teste de notificação SMS"
    )
    assert notificacao_sms.destinatario == "123456789"
    assert notificacao_sms.mensagem == "Teste de notificação SMS"
    assert notificacao_sms.enviar() == "Notificação SMS enviada para 123456789: Teste de notificação SMS"


def test_classe_abstrata():
    with pytest.raises(TypeError):
        NotificacaoSMS(
            destinatario="123456789",
            mensagem="Teste de notificação SMS"
        )  