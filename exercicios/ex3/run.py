from functools import wraps


def registrar_execucao(funcao):
    @wraps(funcao)
    def wrapper(*args, **kwargs):
        print(f"Iniciando execução da função: {funcao.__name__}...")

        resultado = funcao(*args, **kwargs)

        print("Execução finalizada.")
        return resultado

    return wrapper


@registrar_execucao
def enviar_email(destinatario):
    print(f"E-mail enviado para {destinatario}")


@registrar_execucao
def gerar_relatorio(nome):
    print(f"Relatório '{nome}' foi gerado.")


enviar_email("cliente@email.com")

print()

gerar_relatorio("Relatório de Vendas")