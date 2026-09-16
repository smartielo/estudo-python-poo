from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def exibir_dados(self):
        print(f"Nome: {self.nome}, Salário Base: {self.salario_base}")

    @abstractmethod
    def calcular_salario(self):
        pass

class FuncionarioCLT(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def calcular_salario(self):

        salario_total = self.salario_base + self.bonus
        return salario_total


class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, salario_base, percentual_comissao, total_vendas):
        super().__init__(nome, salario_base)
        self.percentual_comissao = percentual_comissao
        self.total_vendas = total_vendas

    def calcular_salario(self):
        comissao = self.total_vendas * self.percentual_comissao
        return self.salario_base + comissao

class Estagiario(Funcionario):
    def __init__(self, nome, salario_base, bolsa_auxilio):
        super().__init__(nome, salario_base)
        self.bolsa_auxilio = bolsa_auxilio

    def calcular_salario(self):
        return self.salario_base + self.bolsa_auxilio



funcionario_clt = FuncionarioCLT("João", 3000.0, 500.0)
funcionario_comissionado = FuncionarioComissionado("Maria", 2000.0, 0.1, 10000.0)   
estagiario = Estagiario("Carlos", 1000.0, 300.0)

funcionario_clt.exibir_dados()
print(f"Salário Total: {funcionario_clt.calcular_salario()}")

funcionario_comissionado.exibir_dados()
print(f"Salário Total: {funcionario_comissionado.calcular_salario()}")

estagiario.exibir_dados()
print(f"Salário Total: {estagiario.calcular_salario()}")