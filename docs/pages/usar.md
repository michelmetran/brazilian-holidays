A maneira mais simples é obter todos os feriados para um determinado ano. Dessa forma os atributos serão definidos por
padrão.

```{.python linenums="1" title="arquivo.py"}
from feriados_brasileiros import datas

# Adiciona todos os feriados de um determinado ano
feriados = datas.Feriados(ano=2023)
feriados.add_all()
feriados
```



<br>

---


## Detalhes

É possível usar a ferramenta de uma maneira mais customizada, onde é possível ajustar todos os atributos para cada um
dos feriados.

Dentre os atributos existentes estão:

- `nome_alternativo`: Nome do Feriado;
- `feriado`: Indica se é feriado ou apenas uma data que usualmente "enforca-se", porém não é feriado formalmente (
  exemplo: véspera de natal e quarta-feira de cinzas);
- `obs`: Campo para observações quaisquer;

```{.python linenums="1" title="arquivo.py"}
from feriados_brasileiros import datas

# Adiciona apenas um feriado de um determinado ano
feriados = datas.Feriados(ano=2023)
feriados.add(nome='Sexta-feira Santa', nome_alternativo='Paixão de Cristo',
             obs='Também conhecido como Sexta-feira Santa')
feriados
```

<br>

---

## Remoção

É possível remover feriados específicos, após ter adicionado todos!

```{.python linenums="1" title="arquivo.py"}
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

