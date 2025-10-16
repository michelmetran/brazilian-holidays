# Brazilian Holidays

[![Repo](https://img.shields.io/badge/GitHub-repo-blue?logo=github&logoColor=f5f5f5)](https://github.com/michelmetran/brazilian-holidays)
[![PyPI - Version](https://img.shields.io/pypi/v/brazilian-holidays?logo=pypi&label=PyPI&color=blue)](https://pypi.org/project/brazilian-holidays/)<br>
[![Read the Docs](https://img.shields.io/readthedocs/brazilian-holidays?logo=ReadTheDocs&label=Read%20The%20Docs)](https://brazilian-holidays.readthedocs.io/)
[![Publish Python to PyPI](https://github.com/michelmetran/brazilian-holidays/actions/workflows/publish-to-pypipoetry.yml/badge.svg)](https://github.com/michelmetran/brazilian-holidays/actions/workflows/publish-to-pypipoetry.yml)

<br>

> _Adoro um feriado! Quem não gosta?!_

Com objetivo de listar os feriados brasileiros, criei o pacote **feriados-brasileiros**, que permite criar uma tabela contendo todos os feriados de um determinado ano, bem como ajustar atributos conforme a necessidade.

A opção por ajustar atributos se deve ao fato de que, nem sempre, um feriado em uma instituição também é feriado n'outra! Feriado de endoeças, por exemplo, é feriado em instituições do meio jurídico, enquanto muitos nem sabem que feriado é esse!

É possível ajustar o nome dos feriados e até mesmo um campo de observações!

<br>

---

| date                | dia_semana    | name                               | holiday | type  | obs                             |
| :------------------ | :------------ | :--------------------------------- | :------ | :---- | :------------------------------ |
| 2024-01-01 00:00:00 | Segunda-feira | Confraternização Universal         | True    | Fixo  |                                 |
| 2024-01-25 00:00:00 | Quinta-feira  | Aniversário da Cidade de São Paulo | True    | Fixo  |                                 |
| 2024-02-12 00:00:00 | Segunda-feira | Carnaval (seg)                     | True    | Móvel |                                 |
| 2024-02-13 00:00:00 | Terça-feira   | Carnaval (ter)                     | True    | Móvel |                                 |
| 2024-02-14 00:00:00 | Quarta-feira  | Carnaval (qua)                     | True    | Móvel |                                 |
| 2024-03-24 00:00:00 | Domingo       | Domingo de Ramos                   | False   | Móvel |                                 |
| 2024-03-28 00:00:00 | Quinta-feira  | Endoenças                          | True    | Móvel |                                 |
| 2024-03-29 00:00:00 | Sexta-feira   | Sexta-feira Santa                  | True    | Móvel |                                 |
| 2024-03-31 00:00:00 | Domingo       | Páscoa                             | True    | Móvel |                                 |
| 2024-04-21 00:00:00 | Domingo       | Tiradentes                         | True    | Fixo  |                                 |
| 2024-05-01 00:00:00 | Quarta-feira  | Dia do Trabalho                    | True    | Fixo  |                                 |
| 2024-05-30 00:00:00 | Quinta-feira  | Corpus Christ                      | True    | Móvel |                                 |
| 2024-06-13 00:00:00 | Quinta-feira  | Santo Antonio                      | True    | Fixo  | Feriado Municipal de Piracicaba |
| 2024-07-09 00:00:00 | Terça-feira   | Revolução Constitucionalista       | True    | Fixo  | Feriado Estadual                |
| 2024-09-07 00:00:00 | Sábado        | Independência do Brasil            | True    | Fixo  |                                 |
| 2024-10-12 00:00:00 | Sábado        | Dia de Nossa Senhora Aparecida     | True    | Fixo  |                                 |
| 2024-10-28 00:00:00 | Segunda-feira | Dia do Servidor Público            | True    | Fixo  |                                 |
| 2024-11-02 00:00:00 | Sábado        | Dia de Finados                     | True    | Fixo  |                                 |
| 2024-11-15 00:00:00 | Sexta-feira   | Proclamação da República           | True    | Fixo  |                                 |
| 2024-11-20 00:00:00 | Quarta-feira  | Dia da Consciência Negra           | True    | Fixo  |                                 |
| 2024-11-20 00:00:00 | Quarta-feira  | Zumbi dos Palmares                 | True    | Fixo  | Feriado Municipal de Piracicaba |
| 2024-12-08 00:00:00 | Domingo       | Imaculada Conceição                | True    | Fixo  | Feriado Municipal de Piracicaba |
| 2024-12-24 00:00:00 | Terça-feira   | Véspera de Natal                   | True    | Fixo  |                                 |
| 2024-12-25 00:00:00 | Quarta-feira  | Natal                              | True    | Fixo  |                                 |
| 2024-12-31 00:00:00 | Terça-feira   | Reveillon                          | True    | Fixo  |                                 |
