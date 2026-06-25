## Classe: Pessoa
### Descrição
Representa uma pessoa com nome, idade e e‑mail. Possui métodos para saudar e validar o e‑mail.

### Atributos
| Nome | Tipo | Descrição |
|------|------|-----------|
| `nome` | `str` | Nome completo da pessoa. |
| `idade` | `int` | Idade em anos. |
| `email` | `str` | Endereço de e‑mail (deve conter `@`). |

### Métodos
| Nome | Assinatura | Parâmetros | Descrição |
|------|------------|------------|-----------|
| `saudacao` | `def saudacao(self) -> str` | — | Retorna uma string de saudação contendo `nome`. |
| `eh_email_valido` | `def eh_email_valido(self) -> bool` | — | Verifica se o atributo `email` contém o caractere `@`. |
| `alterar_nome` | `def alterar_nome(self, novo_nome: str) -> None` | `novo_nome` – novo nome a ser atribuído. | Atualiza o atributo `nome`. |

### Casos de uso típicos
