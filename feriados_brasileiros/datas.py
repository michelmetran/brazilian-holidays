"""
Feriados do Brasil
"""

from datetime import date, datetime, timedelta

import pandas as pd


class Feriados:
    """
    Classe para manejar feriados brasileiros,
    Sendo possível listar, adicionar, criar tabelas, alterar atributos etc.
    """

    def __init__(self, ano, date_format='%d.%m.%Y'):
        # Variables
        self.ano = ano
        self.date_format = date_format

        # Calculate Parameters
        self._realizar_calculo()

        # Monta a data exata da Páscoa no Ano
        dt_pascoa = date(self.ano, self.mes, self.dia)

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
                'data': dt_carnaval_seg,
                'nome_alternativo': None,
                'feriado': True,
                'tipo': 'Móvel',
                'obs': '',
            },
            'Carnaval (ter)': {
                'data': dt_carnaval_ter,
                'nome_alternativo': None,
                'feriado': True,
                'tipo': 'Móvel',
                'obs': '',
            },
            'Carnaval (qua)': {
                'data': dt_carnaval_qua,
                'nome_alternativo': None,
                'feriado': True,
                'tipo': 'Móvel',
                'obs': '',
            },
            'Domingo de Ramos': {
                'data': dt_dom_ramos,
                'nome_alternativo': None,
                'feriado': False,
                'tipo': 'Móvel',
                'obs': '',
            },
            'Páscoa': {
                'data': dt_pascoa,
                'nome_alternativo': None,
                'feriado': True,
                'tipo': 'Móvel',
                'obs': '',
            },
            'Sexta-feira Santa': {
                'data': dt_paixao_cristo,
                'nome_alternativo': None,
                'feriado': True,
                'tipo': 'Móvel',
                'obs': '',
            },
            'Endoenças': {
                'data': dt_endoencas,
                'nome_alternativo': None,
                'feriado': True,
                'tipo': 'Móvel',
                'obs': '',
            },
            'Corpus Christ': {
                'data': dt_corpus_christ,
                'nome_alternativo': None,
                'feriado': True,
                'tipo': 'Móvel',
                'obs': '',
            },
            # Fixo
            'Confraternização Universal': {
                'data': date(self.ano, 1, 1),
                'nome_alternativo': None,
                'feriado': True,
                'tipo': 'Fixo',
                'obs': '',
            },
            'Aniversário da Cidade de São Paulo': {
                'data': date(self.ano, 1, 25),
                'nome_alternativo': None,
                'feriado': True,
                'tipo': 'Fixo',
                'obs': '',
            },
            'Tiradentes': {
                'data': date(self.ano, 4, 21),
                'nome_alternativo': None,
                'feriado': True,
                'tipo': 'Fixo',
                'obs': '',
            },
            'Dia do Trabalho': {
                'data': date(self.ano, 5, 1),
                'nome_alternativo': None,
                'feriado': True,
                'tipo': 'Fixo',
                'obs': '',
            },
            'Independência do Brasil': {
                'data': date(self.ano, 9, 7),
                'nome_alternativo': None,
                'feriado': True,
                'tipo': 'Fixo',
                'obs': '',
            },
            'Dia de Nossa Senhora Aparecida': {
                'data': date(self.ano, 10, 12),
                'nome_alternativo': None,
                'feriado': True,
                'tipo': 'Fixo',
                'obs': '',
            },
            'Dia de Finados': {
                'data': date(self.ano, 11, 2),
                'nome_alternativo': None,
                'feriado': True,
                'tipo': 'Fixo',
                'obs': '',
            },
            'Proclamação da República': {
                'data': date(self.ano, 11, 15),
                'nome_alternativo': None,
                'feriado': True,
                'tipo': 'Fixo',
                'obs': '',
            },
            'Dia da Consciência Negra': {
                'data': date(self.ano, 11, 20),
                'nome_alternativo': None,
                'feriado': True,
                'tipo': 'Fixo',
                'obs': '',
            },
            'Véspera de Natal': {
                'data': date(self.ano, 12, 24),
                'nome_alternativo': None,
                'feriado': True,
                'tipo': 'Fixo',
                'obs': '',
            },
            'Natal': {
                'data': date(self.ano, 12, 25),
                'nome_alternativo': None,
                'feriado': True,
                'tipo': 'Fixo',
                'obs': '',
            },
            'Reveillon': {
                'data': date(self.ano, 12, 31),
                'nome_alternativo': None,
                'feriado': True,
                'tipo': 'Fixo',
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

        p1 = (19 * (self.ano % 19) + 24) % 30
        p2 = (2 * (self.ano % 4) + 4 * (self.ano % 7) + 6 * p1 + 5) % 7
        res = p1 + p2
        if res > 9:
            self.dia = res - 9
            self.mes = 4
        else:
            self.dia = res + 22
            self.mes = 3

    def add(self, nome, nome_alternativo=None, feriado=None, obs=''):
        """
        Adiciona feriado

        :param nome: Nome do feriado
        :type nome: string
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

        if nome not in self.feriados_disponiveis:
            fer = '\n'.join(self.feriados_disponiveis)
            raise Warning(
                f'O feriado precisa ser um dos listados abaixo\n{fer}'
            )

        # Pega o Tipo do Feriado no dict padrão!
        if feriado is None:
            feriado = self.dict_tipo[nome]['feriado']

        # Se não tem nome alternativo, usa o nome
        if nome_alternativo is None:
            nome_alternativo = nome

        # Cria Dicionário
        dict_feriado = {
            nome: {
                'data': self.dict_tipo[nome]['data'],
                'nome_alternativo': nome_alternativo,
                'feriado': feriado,
                'tipo': self.dict_tipo[nome]['tipo'],
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
        return self.dict_tipo[nome]['data']

    def add_all(self):
        """
        Adiciona todos os feriados, com as descrições,
        observações e atributos "padrão"
        :return:
        """

        for feriado in self.feriados_disponiveis:
            self.add(nome=feriado)

    def add_custom(self, nome, mes, dia, feriado, tipo, obs=None):
        """
        Adiciona um feriado "customizado".
        Ideal para feriados municipais,
        não disponíveis no atributo "feriados_disponiveis"

        :param nome: Nome do feriado
        :type nome: string
        :param mes: Número do mês do feriado
        :type mes: int
        :param dia: Número do dia do feriado
        :type dia: int
        :param feriado: Define se é, ou não, feriado (True/False)
        :type feriado: bool
        :param tipo: tipo "Fixo" ou "Móvel"
        :type tipo: string
        :param obs: Acrescenta uma observação ao feriado, defaults to None
        :type obs: string, optional
        :return: Retorna a data do feriado
        :rtype: date
        """
        if mes not in range(1, 13):
            raise Warning('Mês precisa ser menor que 12')

        if dia not in range(1, 31):
            raise Warning('Dia precisa ser menor que 31')

        if tipo not in ['Fixo', 'Móvel']:
            raise Warning('O feriado precisa ser do tipo "Fixo" ou "Móvel"')

        data = date(self.ano, mes, dia)

        # Cria Dicionário
        dict_feriado = {
            nome: {
                'data': data,
                'nome_alternativo': nome,
                'feriado': feriado,
                'tipo': tipo,
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
        Excluí feriado do objeto "Feraidos".
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
        return feriado_del['data']

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
        df = dataframe.sort_values(['data'], ascending=True)
        df['data'] = pd.to_datetime(df['data'])
        df['dia_semama'] = df['data'].dt.day_name(locale='PT')
        df = df.reset_index(drop=True)
        df = df.rename({'nome_alternativo': 'nome'}, axis=1)
        df = df[['data', 'dia_semama', 'nome', 'feriado', 'tipo', 'obs']]
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
            return [datetime.date(x) for x in df['data']]

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
                for x in df['data']
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
            feriados = '\n'.join(list(df['nome']))
            return f'Existe(m) {len(df)} feriado(s) listado(s):\n{feriados}'


class Calendario:
    """
    Classe para manejar mais de um conjunto de feriados
    Idealizado para trabalhar com feriados de vários anos distintos
    """

    def __init__(self):
        self.tabelas_feriados = None
        pass

    def create_table(self, tabelas_feriados):
        """
        _summary_

        :param tabelas_feriados: _description_
        :type tabelas_feriados: _type_
        :raises Warning: _description_
        :raises Warning: _description_
        :return: _description_
        :rtype: _type_
        """
        if not isinstance(tabelas_feriados, list):
            raise Warning(
                f'O parâmetro de input "tabelas_feriados" precisa ser uma lista!\nFoi passado uma {type(tabelas_feriados)}'
            )

        for item in tabelas_feriados:
            if not isinstance(item, Feriados):
                raise Warning(
                    'Os itens da lista precisam ser objetos do tipo "Feriados"'
                )
        self.tabelas_feriados = tabelas_feriados

        list_dfs = []
        for feriado_table in tabelas_feriados:
            list_dfs.append(feriado_table.create_table())

        df = pd.concat(objs=list_dfs, ignore_index=True)
        df = df.sort_values(['data'], ascending=True)
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
        df = self.create_table(self.tabelas_feriados)

        # Tipos
        if tipo == 'date':
            list_feriados = [datetime.date(x) for x in df['data']]

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
                for x in df['data']
            ]

        # Results
        print(f'Existe(m) {len(list_feriados)} feriado(s)')
        return list_feriados

    def __repr__(self):
        df = self.create_table(self.tabelas_feriados)
        # TODO: Adicionar o ano!
        feriados = '\n'.join(list(df['nome']))
        return f'Existe(m) {len(df)} feriado(s) listado(s):\n{feriados}'


if __name__ == '__main__':
    # Resultados
    feriados = Feriados(ano=2023)
    feriados.add(nome='Natal')
    feriados.add_all()

    # Lista Todos
    feriados = Feriados(ano=2023)
    feriados.add_all()

    # # Lista
    lista_feriados = feriados.create_list(tipo='datetime')
    print(lista_feriados)

    # # Tabela
    df = feriados.create_table()
    print(df)
