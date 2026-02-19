# Brazilian Holidays

[![Repo](https://img.shields.io/badge/GitHub-repo-blue?logo=github&logoColor=f5f5f5)](https://github.com/michelmetran/brazilian-holidays)
[![PyPI - Version](https://img.shields.io/pypi/v/brazilian-holidays?logo=pypi&label=PyPI&color=blue)](https://pypi.org/project/brazilian-holidays/)<br>
[![Read the Docs](https://img.shields.io/readthedocs/brazilian-holidays?logo=ReadTheDocs&label=Read%20The%20Docs)](https://brazilian-holidays.readthedocs.io/)
[![Publish Python to PyPI](https://github.com/michelmetran/brazilian-holidays/actions/workflows/publish-to-pypi-uv.yml/badge.svg)](https://github.com/michelmetran/brazilian-holidays/actions/workflows/publish-to-pypi-uv.yml)

<br>

> _Adoro um feriado! Quem não gosta?!_

Com objetivo de listar os feriados brasileiros, criei o pacote **feriados-brasileiros**, que permite criar uma tabela contendo todos os feriados de um determinado ano, bem como ajustar atributos conforme a necessidade.

A opção por ajustar atributos se deve ao fato de que, nem sempre, um feriado em uma instituição também é feriado n'outra! Feriado de endoeças, por exemplo, é feriado em instituições do meio jurídico, enquanto muitos nem sabem que feriado é esse!

É possível ajustar o nome dos feriados e até mesmo um campo de observações!

<br>

---

| date                | dia_semana    | name                               | holiday | type  | obs                             |
| :------------------ | :------------ | :--------------------------------- | :------ | :---- | :------------------------------ |
| 2025-01-01 00:00:00 | Quarta-feira  | Confraternização Universal         | True    | Fixo  |                                 |
| 2025-01-25 00:00:00 | Sábado        | Aniversário da Cidade de São Paulo | True    | Fixo  |                                 |
| 2025-03-03 00:00:00 | Segunda-feira | Carnaval (seg)                     | True    | Móvel |                                 |
| 2025-03-04 00:00:00 | Terça-feira   | Carnaval (ter)                     | True    | Móvel |                                 |
| 2025-03-05 00:00:00 | Quarta-feira  | Carnaval (qua)                     | True    | Móvel |                                 |
| 2025-04-13 00:00:00 | Domingo       | Domingo de Ramos                   | False   | Móvel |                                 |
| 2025-04-17 00:00:00 | Quinta-feira  | Endoenças                          | True    | Móvel |                                 |
| 2025-04-18 00:00:00 | Sexta-feira   | Sexta-feira Santa                  | True    | Móvel |                                 |
| 2025-04-20 00:00:00 | Domingo       | Páscoa                             | True    | Móvel |                                 |
| 2025-04-21 00:00:00 | Segunda-feira | Tiradentes                         | True    | Fixo  |                                 |
| 2025-05-01 00:00:00 | Quinta-feira  | Dia do Trabalho                    | True    | Fixo  |                                 |
| 2025-06-13 00:00:00 | Sexta-feira   | Santo Antonio                      | True    | Fixo  | Feriado Municipal de Piracicaba |
| 2025-06-19 00:00:00 | Quinta-feira  | Corpus Christi                     | True    | Móvel |                                 |
| 2025-07-09 00:00:00 | Quarta-feira  | Revolução Constitucionalista       | True    | Fixo  | Feriado Estadual                |
| 2025-09-07 00:00:00 | Domingo       | Independência do Brasil            | True    | Fixo  |                                 |
| 2025-10-12 00:00:00 | Domingo       | Dia de Nossa Senhora Aparecida     | True    | Fixo  |                                 |
| 2025-10-28 00:00:00 | Terã§a-feira  | Dia do Servidor Público            | True    | Fixo  |                                 |
| 2025-11-02 00:00:00 | Domingo       | Dia de Finados                     | True    | Fixo  |                                 |
| 2025-11-15 00:00:00 | Sábado        | Proclamação da República           | True    | Fixo  |                                 |
| 2025-11-20 00:00:00 | Quinta-feira  | Dia da Consciência Negra           | True    | Fixo  |                                 |
| 2025-11-20 00:00:00 | Quinta-feira  | Zumbi dos Palmares                 | True    | Fixo  | Feriado Municipal de Piracicaba |
| 2025-12-08 00:00:00 | Segunda-feira | Imaculada Conceição                | True    | Fixo  | Feriado Municipal de Piracicaba |
| 2025-12-24 00:00:00 | Quarta-feira  | Véspera de Natal                   | True    | Fixo  |                                 |
| 2025-12-25 00:00:00 | Quinta-feira  | Natal                              | True    | Fixo  |                                 |
| 2025-12-31 00:00:00 | Quarta-feira  | Reveillon                          | True    | Fixo  |                                 |
