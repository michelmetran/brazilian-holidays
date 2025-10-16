"""
Feriados do Brasil
"""

from datetime import date, datetime, timedelta

import pandas as pd


class Holidays:
    """
    Classe para manejar feriados brasileiros,
    Sendo possível listar, adicionar, criar tabelas, alterar atributos, etc.
    """

    def __init__(self, year, date_format='%d.%m.%Y'):
        # Variables
        self.year = year
        self.date_format = date_format

        # Calculate Parameters
        self._realizar_calculo()

        # Monta a data exata da Páscoa no Ano
        dt_pascoa = date(self.year, self.month, self.day)

        # Carnaval ocorre 47 dias antes (Feriado)
        dt_carnaval_ter = date.fromordinal(dt_pascoa.toordinal() - 47)
        dt_carnaval_seg = date.fromordinal(dt_carnaval_ter.toordinal() - 1)
        dt_carnaval_qua = date.fromordinal(dt_carnaval_ter.toordinal() + 1)
        dt_paixao_cristo = date.fromordinal(dt_pascoa.toordinal() - 2)
        dt_endoencas = date.fromordinal(dt_paixao_cristo.toordinal() - 1)
        dt_corpus_christ = date.fromordinal(dt_pascoa.toordinal() + 60)
        dt_dom_ramos = date.fromordinal(dt_pascoa.toordinal() - 7)

        # dddd
        self.dict_tipo = {
            # Móvel
            'Carnaval (seg)': {
                'date': dt_carnaval_seg,
                'alternative_name': None,
                'holiday': True,
                'type': 'Móvel',
                'obs': '',
            },
            'Carnaval (ter)': {
                'date': dt_carnaval_ter,
                'alternative_name': None,
                'holiday': True,
                'type': 'Móvel',
                'obs': '',
            },
            'Carnaval (qua)': {
                'date': dt_carnaval_qua,
                'alternative_name': None,
                'holiday': True,
                'type': 'Móvel',
                'obs': '',
            },
            'Domingo de Ramos': {
                'date': dt_dom_ramos,
                'alternative_name': None,
                'holiday': False,
                'type': 'Móvel',
                'obs': '',
            },
            'Páscoa': {
                'date': dt_pascoa,
                'alternative_name': None,
                'holiday': True,
                'type': 'Móvel',
                'obs': '',
            },
            'Sexta-feira Santa': {
                'date': dt_paixao_cristo,
                'alternative_name': None,
                'holiday': True,
                'type': 'Móvel',
                'obs': '',
            },
            'Endoenças': {
                'date': dt_endoencas,
                'alternative_name': None,
                'holiday': True,
                'type': 'Móvel',
                'obs': '',
            },
            'Corpus Christ': {
                'date': dt_corpus_christ,
                'alternative_name': None,
                'holiday': True,
                'type': 'Móvel',
                'obs': '',
            },
            # Fixo
            'Confraternização Universal': {
                'date': date(self.year, 1, 1),
                'alternative_name': None,
                'holiday': True,
                'type': 'Fixo',
                'obs': '',
            },
            'Aniversário da Cidade de São Paulo': {
                'date': date(self.year, 1, 25),
                'alternative_name': None,
                'holiday': True,
                'type': 'Fixo',
                'obs': '',
            },
            'Tiradentes': {
                'date': date(self.year, 4, 21),
                'alternative_name': None,
                'holiday': True,
                'type': 'Fixo',
                'obs': '',
            },
            'Dia do Trabalho': {
                'date': date(self.year, 5, 1),
                'alternative_name': None,
                'holiday': True,
                'type': 'Fixo',
                'obs': '',
            },
            'Independência do Brasil': {
                'date': date(self.year, 9, 7),
                'alternative_name': None,
                'holiday': True,
                'type': 'Fixo',
                'obs': '',
            },
            'Dia de Nossa Senhora Aparecida': {
                'date': date(self.year, 10, 12),
                'alternative_name': None,
                'holiday': True,
                'type': 'Fixo',
                'obs': '',
            },
            'Dia de Finados': {
                'date': date(self.year, 11, 2),
                'alternative_name': None,
                'holiday': True,
                'type': 'Fixo',
                'obs': '',
            },
            'Proclamação da República': {
                'date': date(self.year, 11, 15),
                'alternative_name': None,
                'holiday': True,
                'type': 'Fixo',
                'obs': '',
            },
            'Dia da Consciência Negra': {
                'date': date(self.year, 11, 20),
                'alternative_name': None,
                'holiday': True,
                'type': 'Fixo',
                'obs': '',
            },
            'Véspera de Natal': {
                'date': date(self.year, 12, 24),
                'alternative_name': None,
                'holiday': True,
                'type': 'Fixo',
                'obs': '',
            },
            'Natal': {
                'date': date(self.year, 12, 25),
                'alternative_name': None,
                'holiday': True,
                'type': 'Fixo',
                'obs': '',
            },
            'Reveillon': {
                'date': date(self.year, 12, 31),
                'alternative_name': None,
                'holiday': True,
                'type': 'Fixo',
                'obs': '',
            },
        }
        #
        self.feriados_disponiveis = list(self.dict_tipo.keys())
        self.dict_feriados_solicitados = {}

    def _realizar_calculo(self):
        """
        Faz os cálculos para definir os feriados móveis
        Obtido no repositório de Fernando Anselmo
        https://github.dev/fernandoans/problemasPython
        Problema 05
        https://www.youtube.com/watch?v=wbM7YhfcSqs
        """

        p1 = (19 * (self.year % 19) + 24) % 30
        p2 = (2 * (self.year % 4) + 4 * (self.year % 7) + 6 * p1 + 5) % 7
        res = p1 + p2
        if res > 9:
            self.day = res - 9
            self.month = 4
        else:
            self.day = res + 22
            self.month = 3

    def add(self, name, nome_alternativo=None, feriado=None, obs=''):
        """
        Adiciona feriado

        :param name: Nome do feriado
        :type name: string
        :param nome_alternativo: Nome do feriado alternativo, caso queira
        ajustar o nome "padrão", defaults to None
        :type nome_alternativo: string, optional
        :param feriado: Define se é, ou não, feriado (True/False),
        defaults to None
        :type feriado: bool, optional
        :param obs: Acrescenta uma observação ao feriado, defaults to None
        :type obs: string, optional
        :raises Warning: Avalia se o feriado solicitado consta na
          lista dos "feriados_disponiveis"
        :return: Retorna a data do feriado
        :rtype: date
        """

        if name not in self.feriados_disponiveis:
            fer = '\n'.join(self.feriados_disponiveis)
            raise Warning(
                f'O feriado precisa ser um dos listados abaixo\n{fer}'
            )

        # Pega o Tipo do Feriado no dict padrão!
        if feriado is None:
            feriado = self.dict_tipo[name]['holiday']

        # Se não tem nome alternativo, usa o nome
        if nome_alternativo is None:
            nome_alternativo = name

        # Cria Dicionário
        dict_feriado = {
            name: {
                'date': self.dict_tipo[name]['date'],
                'alternative_name': nome_alternativo,
                'holiday': feriado,
                'type': self.dict_tipo[name]['type'],
                'obs': obs,
            }
        }

        # Update Dict
        self.dict_tipo.update(dict_feriado)

        # Feriados Solicitados
        dict_temp = self.dict_feriados_solicitados
        dict_temp.update(dict_feriado)
        self.dict_feriados_solicitados = dict_temp

        # Results
        return self.dict_tipo[name]['date']

    def add_all(self):
        """
        Adiciona todos os feriados, com as descrições,
        observações e atributos "padrão"
        :return:
        """
        for feriado in self.feriados_disponiveis:
            self.add(name=feriado)

    def add_custom(self, name, month, day, holiday, type, obs=None):
        """
        Adiciona um feriado "customizado".
        Ideal para feriados municipais,
        não disponíveis no atributo "feriados_disponiveis"

        :param name: Nome do feriado
        :type name: string
        :param month: Número do mês do feriado
        :type month: int
        :param day: Número do dia do feriado
        :type day: int
        :param holiday: Define se é, ou não, feriado (True/False)
        :type holiday: bool
        :param type: tipo "Fixo" ou "Móvel"
        :type type: string
        :param obs: Acrescenta uma observação ao feriado, defaults to None
        :type obs: string, optional
        :return: Retorna a data do feriado
        :rtype: date
        """
        if month not in range(1, 13):
            raise Warning('Mês precisa ser menor que 12')

        if day not in range(1, 31):
            raise Warning('Dia precisa ser menor que 31')

        if type not in ['Fixo', 'Móvel']:
            raise Warning('O feriado precisa ser do tipo "Fixo" ou "Móvel"')

        data = date(self.year, month, day)

        # Cria Dicionário
        dict_feriado = {
            name: {
                'date': data,
                'alternative_name': name,
                'holiday': holiday,
                'type': type,
                'obs': obs,
            }
        }

        # Feriados Solicitados
        dict_temp = self.dict_feriados_solicitados
        dict_temp.update(dict_feriado)
        self.dict_feriados_solicitados = dict_temp
        return data

    def remove(self, nome):
        """
        Excluí feriado do objeto "Feriados".
        Ideal quando se utiliza a função "add_all", para adicionar todos,
        sendo possível remover um ou outro feriado.

        :param nome: Nome do feriado
        :type nome: string
        :raises Warning: Nome do feriado precisa ser um item dos
        "feriados_disponiveis".
        :return: Data do feriado removido do objeto "Feriados"
        :rtype: date
        """
        if nome not in self.feriados_disponiveis:
            fer = '\n'.join(self.feriados_disponiveis)
            raise Warning(
                f'O feriado precisa ser um dos listados abaixo\n{fer}'
            )
        # Feriados Solicitados
        dict_temp = self.dict_feriados_solicitados
        feriado_del = dict_temp.pop(nome)
        self.dict_feriados_solicitados = dict_temp
        return feriado_del['date']

    def create_table(self):
        """
        Cria uma tabela de Feriados, em formato "pandas",
        contendo os feriados adicionados individualmente,
        ou total (com o método "add_all()").

        Apresenta diversas descrições e atributos que
        podem ser customizadas caso o usuário optei por
        adicionar os feriados individualmente.

        :return: Tabela com Feriados
        :rtype: dataframe
        """
        # Adjust Table
        if len(self.dict_feriados_solicitados) == 0:
            raise Warning('Necessário Adicionar feriados!')

        dataframe = pd.DataFrame.from_dict(
            self.dict_feriados_solicitados, orient='index'
        )
        # df = df[pd.notna(df['data'])]
        df = dataframe.sort_values(['date'], ascending=True)
        df['date'] = pd.to_datetime(df['date'])

        # TODO
        df['dia_semana'] = df['date'].dt.day_name(locale='pt_BR.utf8')

        df = df.reset_index(drop=True)
        df = df.rename({'alternative_name': 'name'}, axis=1)
        df = df[['date', 'dia_semana', 'name', 'holiday', 'type', 'obs']]
        return df

    def create_list(self, tipo='datetime'):
        """
        Cria uma lista de Feriados, em formato "date" ou "datetime",
        contendo os feriados adicionados individualmente,
        ou total (com o método "add_all").

        Ideal para utilizar com a biblioteca "dateutil".

        :param tipo: Tipo de lista, defaults to "datetime"
        :type tipo: str, optional
        :raises Warning: Lista precisa ser "date" ou "datetime"
        :return: Lista dos Feriados
        :rtype: list
        """

        if tipo not in ['date', 'datetime']:
            raise Warning(
                'É necessário que o formato seja "date" ou "datetime"!'
            )

        # Cria Tabela
        df = self.create_table()

        # sss
        if tipo == 'date':
            return [datetime.date(x) for x in df['date']]

        elif tipo == 'datetime':
            return [
                datetime(
                    year=x.year,
                    month=x.month,
                    day=x.day,
                    hour=0,
                    minute=0,
                    second=0,
                )
                for x in df['date']
            ]

    def next_feriado(self):
        """
        Define quando é o próximo feriado,
        a partir do dia de hoje!

        :return: Dia do próximo feriado
        :rtype: date
        """
        # Pega dia de hoje
        data = date.today()
        items = self.create_list(tipo='date')

        # Lista de Datas
        list_res = []
        for x in items:
            list_res.append((x - data).days)

        # ddd
        n_days_holiday = min(n for n in list_res if n > 0)
        return data + timedelta(days=n_days_holiday)

    def __repr__(self):
        if len(self.dict_feriados_solicitados) == 0:
            return 'Não foram adicionados feriados'

        else:
            df = self.create_table()
            feriados = '\n'.join(list(df['name']))
            return f'Existe(m) {len(df)} feriado(s) listado(s):\n{feriados}'


class Calendario:
    """
    Classe para manejar mais de um conjunto de feriados
    Idealizado para trabalhar com feriados de vários anos distintos
    """

    def __init__(self):
        self.tabelas_feriados = []
        pass

    def add(self, tabelas_feriados):
        """
        _summary_

        :param tabelas_feriados: _description_
        :type tabelas_feriados: _type_
        :raises Warning: _description_
        """

        if not isinstance(tabelas_feriados, Holidays):
            raise Warning(
                'Os itens da lista precisam ser objetos do tipo "Feriados"'
            )

        self.tabelas_feriados.append(tabelas_feriados.create_table())

    def create_table(self):
        """
        _summary_

        :param tabelas_feriados: _description_
        :type tabelas_feriados: _type_
        :raises Warning: _description_
        :raises Warning: _description_
        :return: _description_
        :rtype: _type_
        """
        # if not isinstance(tabelas_feriados, list):
        #     raise Warning(
        #         f'O parâmetro de input "tabelas_feriados" precisa ser uma lista!\nFoi passado uma {type(tabelas_feriados)}'
        #     )

        # for item in tabelas_feriados:
        #     if not isinstance(item, Holidays):
        #         raise Warning(
        #             'Os itens da lista precisam ser objetos do tipo "Feriados"'
        #         )
        # self.tabelas_feriados = tabelas_feriados

        # list_dfs = []
        # for feriado_table in self.tabelas_feriados:
        #     list_dfs.append(feriado_table.create_table())

        df = pd.concat(objs=self.tabelas_feriados, ignore_index=True)
        df = df.sort_values(['date'], ascending=True)
        df = df.reset_index(drop=True)
        # self.df = df
        return df

    def create_list(self, tipo='datetime'):
        """
        Cria uma lista de Feriados, em formato datetime,
        contendo os feriados adicionados individualmente,
        ou total (com o método "all()")

        :param tipo: Tipo de lista, defaults to 'datetime'
        :type tipo: str, optional
        :raises Warning: Lista precisa ser 'date' ou 'datetime'
        :return: Lista dos Feriados
        :rtype: list
        """
        if tipo not in ['date', 'datetime']:
            raise Warning(
                'É necessário que o formato seja "date" ou "datetime"!'
            )

        # Cria Tabela
        df = self.create_table()

        # Tipos
        if tipo == 'date':
            list_feriados = [datetime.date(x) for x in df['date']]

        elif tipo == 'datetime':
            list_feriados = [
                datetime(
                    year=x.year,
                    month=x.month,
                    day=x.day,
                    hour=0,
                    minute=0,
                    second=0,
                )
                for x in df['date']
            ]
        else:
            pass

        # Results
        print(f'Existe(m) {len(list_feriados)} feriado(s)')
        return list_feriados

    def __repr__(self):
        if self.tabelas_feriados == []:
            return 'Não existem feriados listados'

        else:
            df = self.create_table()
            # TODO: Adicionar o ano!
            feriados = '\n'.join(list(df['name']))
            return f'Existe(m) {len(df)} feriado(s) listado(s):\n{feriados}'


if __name__ == '__main__':
    import pandas as pd

    import brazilian_holidays

    holidays_23 = brazilian_holidays.Holidays(year=2023)
    holidays_23.add_all()

    holidays_24 = brazilian_holidays.Holidays(year=2024)
    holidays_24.add_all()

    # Resultados
    calendario = brazilian_holidays.Calendario()
    calendario.add(tabelas_feriados=holidays_23)
    calendario.add(tabelas_feriados=holidays_24)
    # print(calendario)
    # print(calendario.tabelas_feriados)

    # Create Table
    df = calendario.create_table()
    print(df.info())
