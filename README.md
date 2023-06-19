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

Dentre os atributos existentes estão:

- `nome`: Nome do Feriado;
- `feriado`: Indica se é feriado ou apenas uma data que usualmente "enforca-se", porém não é feriado formalmente;
- `obs`: Campo para observações quaisquer;

```python
from feriados_brasileiros import Feriados

# Lista Todos dos Feriados de um determinado Ano
feriados = Feriados(ano=2023)
feriados.add_all()
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
feriados.add_carnaval_qua(obs='Entrada no serviço após as 14h!')
feriados.add_endoencas(obs='Endoenças: é feriado isso?!', feriado=False)
feriados.add_paixao_cristo(nome='Sexta-feira Santa', obs='Paixão de Cristo')
feriados.add_pascoa(obs='Quero chocolate!!')
feriados.add_corpus_christ()

# Feriados Fixos
feriados.add_confraternizacao()
feriados.add_aniversario_sao_paulo(feriado=False)
feriados.add_tiradentes()
feriados.add_trabalho()
feriados.add_independencia(obs='Independência ou Morte!')
feriados.add_padroeira()
feriados.add_finados()
feriados.add_proclamacao_republica(obs='Dia de ler sobre o arretado Ruy Barbosa!')
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
lista_feriados = feriados.create_list()
print(lista_feriados)

# Resultado em Tabela (mais informações)
df = feriados.create_table()
print(df.head())
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

1. Ajustar documentação
2. ~~Incluir o dia da semana!~~
3. ~~Implantar classe Calendário para pegar feriados de anos diversos~~
4. ~~Add domingo de ramos~~
