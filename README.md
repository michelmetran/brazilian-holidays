# Feriados Brasileiros

[PyPI](https://pypi.org/project/feriados-brasileiros) | [GitHub](https://github.com/michelmetran/feriados)

<br>

> _Adoro um feriado! Quem não gosta?!_

Com objetivo de listar os feriados brasileiros, criei o pacote **feriados-brasileiros**, que permite criar uma tabela contendo todos os feriados de um determinado ano, bem como ajustar atributos conforme a necessidade.

A opção por ajustar atributos se deve ao fato de que, nem sempre, um feriado em uma instituição também é feriado n'outra! Feriado de endoeças, por exemplo, é feriado em instituições do meio jurídico, enquanto muitos nem sabem que feriado é esse!

É possível ajustar o nome dos feriados e até mesmo um campo de observações!

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

```python
from feriados_brasileiros import datas

# Adiciona todos os feriados de um determinado ano
feriados = datas.Feriados(ano=2023)
feriados.add_all()
feriados
```

<br>

---

## Detalhes

É possível usar a ferramenta de uma maneira mais customizada, onde é possível ajustar todos os atributos para cada um dos feriados.

Dentre os atributos existentes estão:

- `nome_alternativo`: Nome do Feriado;
- `feriado`: Indica se é feriado ou apenas uma data que usualmente "enforca-se", porém não é feriado formalmente (exemplo: véspera de natal e quarta-feira de cinzas);
- `obs`: Campo para observações quaisquer;

```python
from feriados_brasileiros import datas

# Adiciona apenas um feriado de um determinado ano
feriados = datas.Feriados(ano=2023)
feriados.add(nome='Sexta-feira Santa', nome_alternativo='Paixão de Cristo', obs='Também conhecido como Sexta-feira Santa')
feriados
```

<br>

---

## Remoção

É possível remover feriados específicos, após ter adicionado todos!

```python
from feriados_brasileiros import datas

# Adiciona todos os feriados de um determinado ano
feriados = datas.Feriados(ano=2023)
feriados.add_all()
feriados.remove('Domingo de Ramos')
feriados.remove('Endoenças')
feriados
```

<br>

---

## _Custom_

Também é possível adicionar um feriado customizado.

```python
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

<br>

---

## Resultados

Seja qual for a opção escolhida para usar o programa, os resultados podem ser obtidos de duas formas distintas.

```python
# Resultado em Lista
lista_feriados = feriados.create_list(tipo='datetime')
print(lista_feriados)

# Resultado em Tabela (mais informações)
df_feriados = feriados.create_table()
print(df_feriados.head())
```

<br>

---

## Documentação

- [UFRGS: **Cálculo do Dia da Páscoa**](https://www.inf.ufrgs.br/~cabral/Pascoa.html)
- [Problemas e Teoremas: **Script em Python do algoritmo de O’Beirne para calcular a data da Páscoa**](https://problemasteoremas.wordpress.com/2010/02/17/script-em-python-do-algoritmo-de-obeirne-para-calcular-o-dia-e-o-mes-do-domingo-de-pascoa/)
- [YouTube: **Problemas em Python 05 - Cálculo de Datas Móveis**](https://www.youtube.com/watch?v=wbM7YhfcSqs), de Fernando Anselmo. Metodologia que adotei para calcular os feriados móveis nesse projeto.

<br>

---

## _TODO_

1. ~~Ajustar documentação~~
2. ~~Incluir o dia da semana!~~
3. ~~Implantar classe Calendário para pegar feriados de anos diversos~~
4. ~~Add domingo de ramos~~
