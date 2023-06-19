"""
Feriados do Brasil
"""

from datetime import date, datetime

import numpy as np
import pandas as pd


class Feriados:
    """
    _summary_
    """

    def __init__(self, ano, date_format='%d.%m.%Y'):
        # Variables
        self._table = None
        self.ano = ano
        self.date_format = date_format
        self._temp = None

        # Tipo: Móvel
        self.tipo_carnaval_seg = None
        self.tipo_carnaval_ter = None
        self.tipo_carnaval_qua = None
        self.tipo_endoencas = None
        self.tipo_paixao_cristo = None
        self.tipo_pascoa = None
        self.tipo_corpus_christ = None

        # Tipo: Fixo
        self.tipo_confraternizacao = None
        self.tipo_aniversario = None
        self.tipo_trabalho = None
        self.tipo_tiradentes = None
        self.tipo_independencia = None
        self.tipo_padroeira = None
        self.tipo_finados = None
        self.tipo_republica = None
        self.tipo_consciencia = None
        self.tipo_vespera_natal = None
        self.tipo_natal = None
        self.tipo_reveillon = None

        # Feriado: Móvel
        self.feriado_carnaval_seg = None
        self.feriado_carnaval_ter = None
        self.feriado_carnaval_qua = None
        self.feriado_endoencas = None
        self.feriado_paixao_cristo = None
        self.feriado_pascoa = None
        self.feriado_corpus_christ = None

        # Feriado: Fixo
        self.feriado_confraternizacao = None
        self.feriado_aniversario = None
        self.feriado_tiradentes = None
        self.feriado_trabalho = None
        self.feriado_independencia = None
        self.feriado_padroeira = None
        self.feriado_finados = None
        self.feriado_republica = None
        self.feriado_consciencia = None
        self.feriado_vespera_natal = None
        self.feriado_natal = None
        self.feriado_reveillon = None

        # Nome: Móvel
        self.nome_carnaval_seg = None
        self.nome_carnaval_ter = None
        self.nome_carnaval_qua = None
        self.nome_endoencas = None
        self.nome_paixao_cristo = None
        self.nome_pascoa = None
        self.nome_corpus_christ = None

        # Nome: Fixo
        self.nome_confraternizacao = None
        self.nome_aniversario = None
        self.nome_tiradentes = None
        self.nome_trabalho = None
        self.nome_independencia = None
        self.nome_padroeira = None
        self.nome_finados = None
        self.nome_republica = None
        self.nome_consciencia = None
        self.nome_vespera_natal = None
        self.nome_natal = None
        self.nome_reveillon = None

        # Obs: Móvel
        self.obs_carnaval_seg = None
        self.obs_carnaval_ter = None
        self.obs_carnaval_qua = None
        self.obs_endoencas = None
        self.obs_paixao_cristo = None
        self.obs_pascoa = None
        self.obs_corpus_christ = None

        # Obs: Fixo
        self.obs_confraternizacao = None
        self.obs_aniversario = None
        self.obs_tiradentes = None
        self.obs_trabalho = None
        self.obs_independencia = None
        self.obs_padroeira = None
        self.obs_finados = None
        self.obs_republica = None
        self.obs_consciencia = None
        self.obs_vespera_natal = None
        self.obs_natal = None
        self.obs_reveillon = None

        # Data: Móvel
        self.dt_pascoa = np.nan
        self.dt_carnaval_seg = np.nan
        self.dt_carnaval_ter = np.nan
        self.dt_carnaval_qua = np.nan
        self.dt_paixao_cristo = np.nan
        self.dt_endoencas = np.nan
        self.dt_corpus_christ = np.nan

        # Data: Fixo
        self.dt_confraternizacao = np.nan
        self.dt_aniversario = np.nan
        self.dt_tiradentes = np.nan
        self.dt_trabalho = np.nan
        self.dt_independencia = np.nan
        self.dt_padroeira = np.nan
        self.dt_finados = np.nan
        self.dt_republica = np.nan
        self.dt_consciencia = np.nan
        self.dt_vespera_natal = np.nan
        self.dt_natal = np.nan
        self.dt_reveillon = np.nan

        # Calculate Parameters
        # self._realizar_calculo()

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

    def add_all(self):
        """
        Adiciona todos os feriados, com as descrições,
        observações e atributos "padrão"
        """

        # Móveis
        self.add_carnaval_seg()
        self.add_carnaval_qua()
        self.add_endoencas()
        self.add_paixao_cristo()
        self.add_corpus_christ()
        self.add_carnaval_ter()
        self.add_pascoa()

        # Fixos
        self.add_confraternizacao()
        self.add_aniversario_sao_paulo()
        self.add_tiradentes()
        self.add_trabalho()
        self.add_independencia()
        self.add_padroeira()
        self.add_finados()
        self.add_proclamacao_republica()
        self.add_consciencia_negra()
        self.add_vespera_natal()
        self.add_natal()
        self.add_reveillon()

    def table(self):
        """
        Cria uma tabela de Feriados, em formato pandas,
        contendo os feriados adicionados individualmente,
        ou total (com o método "all()").

        Apresenta diversas descrições e atributos que
        podem ser customizadas caso o usuário optei por
        adicioar os feriados indifidualmente.

        :return: Tabela com Feriados
        :rtype: dataframe
        """

        list_feriados = [
            # Móveis
            {
                'data': self.dt_pascoa,
                'nome': self.nome_pascoa,
                'feriado': self.feriado_pascoa,
                'tipo': self.tipo_pascoa,
                'obs': self.obs_pascoa,
            },
            {
                'data': self.dt_carnaval_seg,
                'nome': self.nome_carnaval_seg,
                'feriado': self.feriado_carnaval_seg,
                'tipo': self.tipo_carnaval_seg,
                'obs': self.obs_carnaval_seg,
            },
            {
                'data': self.dt_carnaval_ter,
                'nome': self.nome_carnaval_ter,
                'feriado': self.feriado_carnaval_ter,
                'tipo': self.tipo_carnaval_ter,
                'obs': self.obs_carnaval_ter,
            },
            {
                'data': self.dt_carnaval_qua,
                'nome': self.nome_carnaval_qua,
                'feriado': self.feriado_carnaval_qua,
                'tipo': self.tipo_carnaval_qua,
                'obs': self.obs_carnaval_qua,
            },
            {
                'data': self.dt_paixao_cristo,
                'nome': self.nome_paixao_cristo,
                'feriado': self.feriado_paixao_cristo,
                'tipo': self.tipo_paixao_cristo,
                'obs': self.obs_paixao_cristo,
            },
            {
                'data': self.dt_endoencas,
                'nome': self.nome_endoencas,
                'feriado': self.feriado_endoencas,
                'tipo': self.tipo_endoencas,
                'obs': self.obs_endoencas,
            },
            {
                'data': self.dt_corpus_christ,
                'nome': self.nome_corpus_christ,
                'feriado': self.feriado_corpus_christ,
                'tipo': self.tipo_corpus_christ,
                'obs': self.obs_corpus_christ,
            },
            # Fixos
            {
                'data': self.dt_confraternizacao,
                'nome': self.nome_confraternizacao,
                'feriado': self.feriado_confraternizacao,
                'tipo': self.tipo_confraternizacao,
                'obs': self.obs_confraternizacao,
            },
            {
                'data': self.dt_aniversario,
                'nome': self.nome_aniversario,
                'feriado': self.feriado_aniversario,
                'tipo': self.tipo_aniversario,
                'obs': self.obs_aniversario,
            },
            {
                'data': self.dt_tiradentes,
                'nome': self.nome_tiradentes,
                'feriado': self.feriado_tiradentes,
                'tipo': self.tipo_tiradentes,
                'obs': self.obs_tiradentes,
            },
            {
                'data': self.dt_trabalho,
                'nome': self.nome_trabalho,
                'feriado': self.feriado_trabalho,
                'tipo': self.tipo_trabalho,
                'obs': self.obs_trabalho,
            },
            {
                'data': self.dt_independencia,
                'nome': self.nome_independencia,
                'feriado': self.feriado_independencia,
                'tipo': self.tipo_independencia,
                'obs': self.obs_independencia,
            },
            {
                'data': self.dt_padroeira,
                'nome': self.nome_padroeira,
                'feriado': self.feriado_padroeira,
                'tipo': self.tipo_padroeira,
                'obs': self.obs_padroeira,
            },
            {
                'data': self.dt_finados,
                'nome': self.nome_finados,
                'feriado': self.feriado_finados,
                'tipo': self.tipo_finados,
                'obs': self.obs_finados,
            },
            {
                'data': self.dt_republica,
                'nome': self.nome_republica,
                'feriado': self.feriado_republica,
                'tipo': self.tipo_republica,
                'obs': self.obs_republica,
            },
            {
                'data': self.dt_consciencia,
                'nome': self.nome_consciencia,
                'feriado': self.feriado_consciencia,
                'tipo': self.tipo_consciencia,
                'obs': self.obs_consciencia,
            },
            {
                'data': self.dt_vespera_natal,
                'nome': self.nome_vespera_natal,
                'feriado': self.feriado_vespera_natal,
                'tipo': self.tipo_vespera_natal,
                'obs': self.obs_vespera_natal,
            },
            {
                'data': self.dt_natal,
                'nome': self.nome_natal,
                'feriado': self.feriado_natal,
                'tipo': self.tipo_natal,
                'obs': self.obs_natal,
            },
            {
                'data': self.dt_reveillon,
                'nome': self.nome_reveillon,
                'feriado': self.feriado_reveillon,
                'tipo': self.tipo_reveillon,
                'obs': self.obs_reveillon,
            },
        ]
        # Adjust Table
        df = pd.DataFrame(list_feriados)
        df = df[pd.notna(df['data'])]
        df = df.sort_values(['data'], ascending=True)
        df['data'] = pd.to_datetime(df['data'])
        df['dia_semama'] = df['data'].dt.day_name(locale='PT')
        df = df.reset_index(drop=True)
        df = df[['data', 'dia_semama', 'nome', 'feriado', 'tipo', 'obs']]
        self._table = df
        return self._table

    def list(self):
        """
        Cria uma lista de Feriados, em formato datetime,
        contendo os feriados adicionados individualmente,
        ou total (com o método "all()")

        :return: Lista dos Feriados
        :rtype: list
        """
        #
        df = self.table()
        list_feriados = list(df['data'])

        # Results
        list_feriados = [x for x in list_feriados if pd.notna(x)]
        list_feriados = [datetime.date(x) for x in df['data']]
        print(f'Existe(m) {len(list_feriados)} feriado(s)')
        return list_feriados

    def add_pascoa(self, feriado=True, nome='Páscoa', obs=''):
        """
        _summary_

        :param feriado: _description_, defaults to True
        :type feriado: bool, optional
        :param nome: _description_, defaults to 'Páscoa'
        :type nome: str, optional
        :param obs: _description_, defaults to ''
        :type obs: str, optional
        :return: _description_
        :rtype: _type_
        """
        # Calculate Parameters
        self._realizar_calculo()

        # Atributos
        self.feriado_pascoa = feriado
        self.nome_pascoa = nome
        self.obs_pascoa = obs

        # Monta a data exata da Pásco no Ano
        self.dt_pascoa = date(self.ano, self.mes, self.dia)
        return self.dt_pascoa

    def add_carnaval_ter(
            self,
            feriado=True,
            nome='Carnaval',
            obs='',
    ):
        """
        _summary_

        :param feriado: _description_, defaults to True
        :type feriado: bool, optional
        :param nome: _description_, defaults to 'Carnaval'
        :type nome: str, optional
        :param obs: _description_, defaults to ''
        :type obs: str, optional
        :return: _description_
        :rtype: _type_
        """

        # Atributos
        self.feriado_carnaval_ter = feriado
        self.tipo_carnaval_ter = 'Móvel'
        self.nome_carnaval_ter = nome
        self.obs_carnaval_ter = obs

        self._temp = self.dt_pascoa
        if not isinstance(self.dt_pascoa, date):
            self.add_pascoa()

        # Carnaval ocorre 47 dias antes (Feriado)
        self.dt_carnaval_ter = date.fromordinal(self.dt_pascoa.toordinal() - 47)

        # Retorna para Nulo
        self.dt_pascoa = self._temp

        return self.dt_carnaval_ter

    def add_carnaval_seg(
            self,
            feriado=False,
            nome='Carnaval (Segunda-feira)',
            obs='No Brasil segunda de carnaval é feriado!!',
    ):
        """
        _summary_

        :param feriado: _description_, defaults to False
        :type feriado: bool, optional
        :param nome: _description_, defaults to 'Carnaval (Segunda-feira)'
        :type nome: str, optional
        :param obs: _description_, defaults to 'No Brasil segunda de carnaval é feriado!!'
        :type obs: str, optional
        :return: _description_
        :rtype: _type_
        """

        # Atributos
        self.feriado_carnaval_seg = feriado
        self.tipo_carnaval_seg = 'Móvel'
        self.nome_carnaval_seg = nome
        self.obs_carnaval_seg = obs

        self._temp = self.dt_carnaval_ter
        if not isinstance(self.dt_carnaval_ter, date):
            self.add_carnaval_ter()

        self.dt_carnaval_seg = date.fromordinal(
            self.dt_carnaval_ter.toordinal() - 1
        )

        # Retorna para Nulo
        self.dt_carnaval_ter = self._temp

        return self.dt_carnaval_seg

    def add_carnaval_qua(
            self,
            feriado=False,
            nome='Carnaval (Quarta de Cinzas)',
            obs='Quarta de Cinzas!? Não é feriado!?',
    ):
        """
        _summary_

        :param feriado: _description_, defaults to False
        :type feriado: bool, optional
        :param nome: _description_, defaults to 'Carnaval (Quarta de Cinzas)'
        :type nome: str, optional
        :param obs: _description_, defaults to 'Quarta de Cinzas!? Não é feriado!?'
        :type obs: str, optional
        :return: _description_
        :rtype: _type_
        """

        # Atributos
        self.feriado_carnaval_qua = feriado
        self.tipo_carnaval_qua = 'Móvel'
        self.nome_carnaval_qua = nome
        self.obs_carnaval_qua = obs

        self._temp = self.dt_carnaval_ter
        if not isinstance(self.dt_carnaval_ter, date):
            self.add_carnaval_ter()

        self.dt_carnaval_qua = date.fromordinal(
            self.dt_carnaval_ter.toordinal() + 1
        )

        self.dt_carnaval_ter = self._temp

        return self.dt_carnaval_qua

    def add_paixao_cristo(
            self,
            feriado=True,
            nome='Sexta-feira Santa',
            obs='Também conhecida como Paixão de Cristo',
    ):
        """
        _summary_

        :param feriado: _description_, defaults to True
        :type feriado: bool, optional
        :param nome: _description_, defaults to 'Sexta-feira Santa'
        :type nome: str, optional
        :param obs: _description_, defaults to 'Também conhecida como Paixão de Cristo'
        :type obs: str, optional
        :return: _description_
        :rtype: _type_
        """

        # Atributos
        self.feriado_paixao_cristo = feriado
        self.tipo_paixao_cristo = 'Móvel'
        self.nome_paixao_cristo = nome
        self.obs_paixao_cristo = obs

        self._temp = self.dt_pascoa
        if not isinstance(self.dt_pascoa, date):
            self.add_pascoa()

        self.dt_paixao_cristo = date.fromordinal(self.dt_pascoa.toordinal() - 2)
        self.dt_pascoa = self._temp
        return self.dt_paixao_cristo

    def add_endoencas(
            self,
            feriado=False,
            nome='Endoenças',
            obs='Feriado apenas para algumas instituições',
    ):
        """
        Summary

        :param feriado: _description_, defaults to False
        :type feriado: bool, optional
        :param nome: _description_, defaults to 'Endoenças'
        :type nome: str, optional
        :param obs: _description_, defaults to 'Feriado apenas para algumas instituições'
        :type obs: str, optional
        :return: _description_
        :rtype: _type_
        """

        # Atributos
        self.feriado_endoencas = feriado
        self.tipo_endoencas = 'Móvel'
        self.nome_endoencas = nome
        self.obs_endoencas = obs

        self._temp = self.dt_paixao_cristo
        if not isinstance(self.dt_paixao_cristo, date):
            self.add_paixao_cristo()

        self.dt_endoencas = date.fromordinal(
            self.dt_paixao_cristo.toordinal() - 1
        )
        self.dt_paixao_cristo = self._temp
        return self.dt_endoencas

    def add_corpus_christ(self, feriado=True, nome='Corpus Christ', obs=''):
        """
        _summary_

        :param feriado: _description_, defaults to True
        :type feriado: bool, optional
        :param nome: _description_, defaults to 'Corpus Christ'
        :type nome: str, optional
        :param obs: _description_, defaults to ''
        :type obs: str, optional
        :return: _description_
        :rtype: _type_
        """

        # Atributos
        self.feriado_corpus_christ = feriado
        self.tipo_corpus_christ = 'Móvel'
        self.nome_corpus_christ = nome
        self.obs_corpus_christ = obs
        self._temp = self.dt_pascoa
        if not isinstance(self.dt_pascoa, date):
            self.add_pascoa()

        # Corpus Christ ocorre 60 dias depois
        self.dt_corpus_christ = date.fromordinal(
            self.dt_pascoa.toordinal() + 60
        )
        self.dt_pascoa = self._temp
        return self.dt_corpus_christ

    def add_confraternizacao(
            self, feriado=True, nome='Confraternização Universal', obs=''
    ):
        """
        _summary_

        :param feriado: _description_, defaults to True
        :type feriado: bool, optional
        :param nome: _description_, defaults to 'Confraternização Universal'
        :type nome: str, optional
        :param obs: _description_, defaults to ''
        :type obs: str, optional
        :return: _description_
        :rtype: _type_
        """
        # Atributos
        self.feriado_confraternizacao = feriado
        self.tipo_confraternizacao = 'Fixo'
        self.nome_confraternizacao = nome
        self.obs_confraternizacao = obs
        self.dt_confraternizacao = date(self.ano, 1, 1)
        return self.dt_confraternizacao

    def add_aniversario_sao_paulo(
            self,
            feriado=True,
            nome='Aniversário da Cidade de São Paulo',
            obs='Feriado Municipal',
    ):
        """
        _summary_

        :param feriado: _description_, defaults to True
        :type feriado: bool, optional
        :param nome: _description_, defaults to 'Aniversário da Cidade de São Paulo'
        :type nome: str, optional
        :param obs: _description_, defaults to 'Feriado Municipal'
        :type obs: str, optional
        :return: _description_
        :rtype: _type_
        """
        # Atributos
        self.feriado_aniversario = feriado
        self.tipo_aniversario = 'Fixo'
        self.nome_aniversario = nome
        self.obs_aniversario = obs
        self.dt_aniversario = date(self.ano, 1, 25)
        return self.dt_aniversario

    def add_tiradentes(self, feriado=True, nome='Tiradentes', obs=''):
        """
        _summary_

        :param feriado: _description_, defaults to True
        :type feriado: bool, optional
        :param nome: _description_, defaults to 'Tiradentes'
        :type nome: str, optional
        :param obs: _description_, defaults to ''
        :type obs: str, optional
        :return: _description_
        :rtype: _type_
        """
        # Atributos
        self.feriado_tiradentes = feriado
        self.tipo_tiradentes = 'Fixo'
        self.nome_tiradentes = nome
        self.obs_tiradentes = obs
        self.dt_tiradentes = date(self.ano, 4, 21)
        return self.dt_aniversario

    def add_trabalho(self, feriado=True, nome='Dia do Trabalho', obs=''):
        """
        _summary_

        :param feriado: _description_, defaults to True
        :type feriado: bool, optional
        :param nome: _description_, defaults to 'Dia do Trabalho'
        :type nome: str, optional
        :param obs: _description_, defaults to ''
        :type obs: str, optional
        :return: _description_
        :rtype: _type_
        """
        # Atributos
        self.feriado_trabalho = feriado
        self.tipo_trabalho = 'Fixo'
        self.nome_trabalho = nome
        self.obs_trabalho = obs
        self.dt_trabalho = date(self.ano, 5, 1)
        return self.dt_aniversario

    def add_independencia(
            self, feriado=True, nome='Independência do Brasil', obs=''
    ):
        """
        _summary_

        :param feriado: _description_, defaults to True
        :type feriado: bool, optional
        :param nome: _description_, defaults to 'Independência do Brasil'
        :type nome: str, optional
        :param obs: _description_, defaults to ''
        :type obs: str, optional
        :return: _description_
        :rtype: _type_
        """
        # Atributos
        self.feriado_independencia = feriado
        self.tipo_independencia = 'Fixo'
        self.nome_independencia = nome
        self.obs_independencia = obs
        self.dt_independencia = date(self.ano, 9, 7)
        return self.dt_aniversario

    def add_padroeira(
            self,
            feriado=True,
            nome='Nossa Sra. Aparecida',
            obs='Padroeira do Brasil',
    ):
        """
        _summary_

        :param feriado: _description_, defaults to True
        :type feriado: bool, optional
        :param nome: _description_, defaults to 'Nossa Sra. Aparecida'
        :type nome: str, optional
        :param obs: _description_, defaults to 'Padroeira do Brasil'
        :type obs: str, optional
        :return: _description_
        :rtype: _type_
        """
        # Atributos
        self.feriado_padroeira = feriado
        self.tipo_padroeira = 'Fixo'
        self.nome_padroeira = nome
        self.obs_padroeira = obs
        self.dt_padroeira = date(self.ano, 10, 12)
        return self.dt_padroeira

    def add_finados(self, feriado=True, nome='Dia de Finados', obs=''):
        """
        _summary_

        :param feriado: _description_, defaults to True
        :type feriado: bool, optional
        :param nome: _description_, defaults to 'Dia de Finados'
        :type nome: str, optional
        :param obs: _description_, defaults to ''
        :type obs: str, optional
        :return: _description_
        :rtype: _type_
        """
        # Atributos
        self.feriado_finados = feriado
        self.tipo_finados = 'Fixo'
        self.nome_finados = nome
        self.obs_finados = obs
        self.dt_finados = date(self.ano, 11, 2)
        return self.dt_finados

    def add_proclamacao_republica(
            self, feriado=True, nome='Proclamação da República', obs=''
    ):
        """
        _summary_

        :param feriado: _description_, defaults to True
        :type feriado: bool, optional
        :param nome: _description_, defaults to 'Proclamação da República'
        :type nome: str, optional
        :param obs: _description_, defaults to ''
        :type obs: str, optional
        :return: _description_
        :rtype: _type_
        """
        # Atributos
        self.feriado_republica = feriado
        self.tipo_republica = 'Fixo'
        self.nome_republica = nome
        self.obs_republica = obs
        self.dt_republica = date(self.ano, 11, 15)
        return self.dt_republica

    def add_consciencia_negra(
            self,
            feriado=False,
            nome='Dia da Consciência Negra',
            obs='Feriado Municipal',
    ):
        """
        _summary_

        :param feriado: _description_, defaults to False
        :type feriado: bool, optional
        :param nome: _description_, defaults to 'Dia da Consciência Negra'
        :type nome: str, optional
        :param obs: _description_, defaults to 'Feriado Municipal'
        :type obs: str, optional
        :return: _description_
        :rtype: _type_
        """
        # Atributos
        self.feriado_consciencia = feriado
        self.tipo_consciencia = 'Fixo'
        self.nome_consciencia = nome
        self.obs_consciencia = obs
        self.dt_consciencia = date(self.ano, 11, 20)
        return self.dt_consciencia

    def add_vespera_natal(self, feriado=False, nome='Vérpera de Natal', obs=''):
        """
        _summary_

        :param feriado: _description_, defaults to False
        :type feriado: bool, optional
        :param nome: _description_, defaults to 'Vérpera de Natal'
        :type nome: str, optional
        :param obs: _description_, defaults to ''
        :type obs: str, optional
        :return: _description_
        :rtype: _type_
        """
        # Atributos
        self.feriado_vespera_natal = feriado
        self.tipo_vespera_natal = 'Fixo'
        self.nome_vespera_natal = nome
        self.obs_vespera_natal = obs
        self.dt_vespera_natal = date(self.ano, 12, 24)
        return self.dt_vespera_natal

    def add_natal(self, feriado=True, nome='Natal', obs=''):
        """
        _summary_

        :param feriado: _description_, defaults to True
        :type feriado: bool, optional
        :param nome: _description_, defaults to 'Natal'
        :type nome: str, optional
        :param obs: _description_, defaults to ''
        :type obs: str, optional
        :return: _description_
        :rtype: _type_
        """
        # Atributos
        self.feriado_natal = feriado
        self.tipo_natal = 'Fixo'
        self.nome_natal = nome
        self.obs_natal = obs
        self.dt_natal = date(self.ano, 12, 25)
        return self.dt_natal

    def add_reveillon(
            self, feriado=False, nome='Reveillon', obs='Não é feriado!?'
    ):
        """
        _summary_

        :param feriado: _description_, defaults to False
        :type feriado: bool, optional
        :param nome: _description_, defaults to 'Reveillon'
        :type nome: str, optional
        :param obs: _description_, defaults to 'Não é feriado!?'
        :type obs: str, optional
        :return: _description_
        :rtype: _type_
        """
        # Atributos
        self.feriado_reveillon = feriado
        self.tipo_reveillon = 'Fixo'
        self.nome_reveillon = nome
        self.obs_reveillon = obs
        self.dt_reveillon = date(self.ano, 12, 31)
        return self.dt_reveillon

    def __repr__(self):
        if self._table is None:
            return f'Existe 0 feriados listados'
        else:
            return f'Existe {len(self._table)} feriados listados'


if __name__ == '__main__':
    from paths import data_path

    # Resultados
    ANO = 2023
    feriados = Feriados(ano=ANO)

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
    feriados.add_aniversario_sao_paulo()
    feriados.add_tiradentes()
    feriados.add_trabalho()
    feriados.add_independencia()
    feriados.add_padroeira()
    feriados.add_finados()
    feriados.add_proclamacao_republica()
    feriados.add_consciencia_negra()
    feriados.add_vespera_natal()
    feriados.add_natal()
    feriados.add_reveillon()

    # Lista Todos
    feriados = Feriados(ano=2023)
    feriados.add_all()

    # Lista
    lista_feriados = feriados.list()
    print(lista_feriados)

    # # Tabela
    df = feriados.table()
    df.to_csv(data_path / f'feriados_{ANO}.csv', index=False)
    print(df)
