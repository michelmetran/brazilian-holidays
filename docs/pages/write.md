## Mark

- [ ] dffff
- [ ] ffffff

<br>

---

## Emoji

:snake:

<br>

---

## Code

```{.python linenums="1" title="arquivo.py"}
import os

def fdfdfd():
    return 1
```

<br>

Também é possível adicionar um feriado customizado.

```{.python linenums="1" title="arquivo.py"}
from feriados_brasileiros import datas

# Adiciona todos os feriados de um determinado ano, além de outras feriados customizados (municipais e estaduais, por exemplo)
feriados = datas.Feriados(ano=2023)
feriados.add_all()
feriados.add_custom(
    nome='Dia do Servidor Público',
    mes=10,
    dia=28,
    feriado=True,
    tipo='Fixo',
)
feriados
```

---

## Diagrams

To create diagrams using _meirmaid_,

- https://squidfunk.github.io/mkdocs-material/reference/diagrams/

Necessário usar o código no `mkdocs.yml`

```
markdown_extensions:
  - pymdownx.emoji # Suporte a emojis
  - pymdownx.tasklist # Suporte à tarefas
  - pymdownx.mark # Marcado
  - pymdownx.tilde  # Realçado
  - pymdownx.highlight  # Código
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
```

<br>

Dai ele renderiza abaixo

```mermaid
graph LR
  A[Start] --> B{Error?};
  B -->|Yes| C[Hmm...];
  C --> D[Debug];
  D --> B;
  B ---->|No| E[Yay!];
```
