# Feriados Brasileiros

[PyPI](https://pypi.org/search/?q=feriados) | [GitHub](https://github.com/michelmetran/feriados)

<br>

---

## Como Instalar?!

```python
pip3 install feriados-brasileiros
```

<br>

---

## Como Usar?!

A maneira mais simples é obter todos os feriados para um determinado ano. Dessa forma os atributos serão definidos por padrão.

Dentre os atributos existentes estão:

- `nome`: Nome do Feriado;
- `feriado`: Indica se é feriado ou apenas uma data que usualmente "enforca-se", porém não é feriado formalmente;
- `obs`: Campo para observações quaisquer;

```python
from feriados_brasileiros import Feriados

# Lista Todos dos Feriados de um determinado Ano
feriados = Feriados(ano=2023)
feriados.all()
```

<br>

---

## Detalhes

É possível usar a ferramenta de uma maneira mais customizada, onde é possível ajustar todos os atributos (`nome`, `feriado`, `obs`) para cada um dos feriados.

```python
# Lista Todos dos Feriados de um determinado Ano
feriados = Feriados(ano=2023)

# Feriados Móveis
feriados.add_carnaval_seg(nome='Segundona de Carnaval!')
feriados.add_carnaval_ter()
feriados.add_carnaval_qua(obs='Diz que é feriado vai!')
feriados.add_endoencas(obs='Endoenças?! Que isso!', feriado=False)
feriados.add_paixao_cristo(nome='Sexta-feira Santa')
feriados.add_pascoa(obs='Eu só quero chocolate!')
feriados.add_corpus_christ()

# Feriados Fixos
feriados.add_confraternizacao()
feriados.add_aniversario_sao_paulo(feriado=False)
feriados.add_tiradentes()
feriados.add_trabalho()
feriados.add_independencia(obs='Independência ou Morte!')
feriados.add_padroeira()
feriados.add_finados()
feriados.add_proclamacao_republica()
feriados.add_consciencia_negra()
feriados.add_vespera_natal(feriado=False)
feriados.add_natal()
feriados.add_reveillon(feriado=False)
```

<br>

---

## Resultados

Seja qual for a opção escolhida para usar o programa, os resultados podem ser obtidos de duas formas distintas.

```python
# Resultado em Lista
lista_feriados = feriados.list()
print(lista_feriados)

# Resultado em Tabela (mais informações)
df = feriados.table()
print(df.head())
```

<br>

---

## _TODO_

1. Ajustar documentação
2. Incluir o dia da semana!
3. Implantar classe Calndario para pegar feriados de anos diversos


