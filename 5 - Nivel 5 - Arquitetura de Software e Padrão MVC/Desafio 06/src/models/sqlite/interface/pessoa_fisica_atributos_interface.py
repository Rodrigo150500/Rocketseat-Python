class PessoaFisicaInterface:
    def __init__(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
        self.renda_mensal = renda_mensal
        self.idade = idade
        self.nome_completo = nome_completo
        self.celular = celular
        self.email = email
        self.categoria = categoria
        self.saldo = saldo