"""Módulo que contém a classe :class:`Pessoa`."""

class Pessoa:
    """
    Representa uma pessoa simples.

    Attributes:
        nome (str): Nome completo da pessoa.
        idade (int): Idade em anos.
        email (str): Endereço de e‑mail.
    """

    def __init__(self, nome: str, idade: int, email: str) -> None:
        """
        Inicializa uma nova instância de :class:`Pessoa`.

        Args:
            nome: Nome completo da pessoa.
            idade: Idade da pessoa (deve ser não‑negativa).
            email: Endereço de e‑mail válido.
        """
        self.nome = nome
        self.idade = idade
        self.email = email

    def __str__(self) -> str:
        """Retorna uma representação legível da instância."""
        return f"Pessoa({self.nome}, {self.idade})"

    def saudacao(self) -> str:
        """Retorna uma mensagem de saudação contendo o nome da pessoa."""
        return f"Olá, {self.nome}!"

    def eh_email_valido(self) -> bool:
        """Verifica se o atributo ``email`` contém o caractere ``@``."""
        return "@" in self.email

    def alterar_nome(self, novo_nome: str) -> None:
        """
        Altera o atributo ``nome`` da instância.

        Args:
            novo_nome: Novo nome a ser atribuído.
        """
        self.nome = novo_nome
