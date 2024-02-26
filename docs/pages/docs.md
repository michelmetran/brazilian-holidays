# Documentação

## MkDocs

Teste 



<br>

------

## Read the Docs

<br>

------

## Diagramas

Para fazer diagramas usando o meirmaid, 
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
``` mermaid
graph LR
  A[Start] --> B{Error?};
  B -->|Yes| C[Hmm...];
  C --> D[Debug];
  D --> B;
  B ---->|No| E[Yay!];
```

