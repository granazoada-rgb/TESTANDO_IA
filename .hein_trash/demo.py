"""Exemplo de uso da classe :class:`Pessoa`."""

from pessoa import Pessoa

def main() -> None:
    # Cria uma instância de Pessoa
    joao = Pessoa(nome="João da Silva", idade=32, email="joao@email.com")

    # Exibe informações básicas
    print(joao)                     # → Pessoa(João da Silva, 32)
    print(joao.saudacao())          # → Olá, João da Silva!

    # Verifica se o e‑mail está válido
    print("E‑mail válido?", joao.eh_email_valido())  # → True

    # Altera o nome e mostra o novo objeto
    joao.alterar_nome("João S.")
    print("Novo nome:", joao)       # → Pessoa(João S., 32)
    
if __name__ == "__main__":
    main()
