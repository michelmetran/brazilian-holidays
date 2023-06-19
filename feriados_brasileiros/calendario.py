"""
_summary_

:raises Warning: _description_
:return: _description_
:rtype: _type_
"""

from datetime import datetime

import pandas as pd

from feriados import Feriados


class Calendario(Feriados):
    """
    _summary_

    :param Feriados: _description_
    :type Feriados: _type_
    """

    def __init__(self, ano, date_format='%d.%m.%Y'):
        super().__init__(ano, date_format)

        list_dfs = []
        if isinstance(self.ano, int):
            print('é inteiro')
            for i in [self.ano]:
                feriadosd = Feriados(ano=i)
                feriadosd.all()
                df = feriadosd.table()
                list_dfs.append(df)
                self.list_dfs = list_dfs

        if isinstance(self.ano, tuple):
            print('é tupla')
            if not self.ano[0] <= self.ano[1]:
                raise Warning(
                    f'\nPrimeira data ({self.ano[0]}) deve ser menor que segunda data ({self.ano[1]}).\nSugestão: insira ({self.ano[1]}, {self.ano[0]})'
                )
            # Loops
            for i in range(self.ano[0], self.ano[1] + 1):
                feriadosd = Feriados(ano=i)
                feriadosd.all()
                df = feriadosd.table()
                list_dfs.append(df)
                self.list_dfs = list_dfs

        if isinstance(self.ano, list):
            print('é lista')
            # Loops
            for i in self.ano:
                feriadosd = Feriados(ano=i)
                feriadosd.all()
                df = feriadosd.table()
                list_dfs.append(df)
                self.list_dfs = list_dfs

    def feriados(self):
        df = pd.concat(objs=self.list_dfs, ignore_index=True)
        df = df.sort_values(['data'], ascending=True)
        df = df.reset_index(drop=True)
        print(df.data.min(), df.data.max())
        return df

    def all_lists(self):
        df = self.feriados()
        list_feriados = list(df['data'])

        # Results
        list_feriados = [x for x in list_feriados if pd.notna(x)]
        list_feriados = [datetime.date(x) for x in df['data']]
        print(f'Existe(m) {len(list_feriados)} feriado(s)')
        return list_feriados


if __name__ == '__main__':
    cal = Calendario(ano=2014)
    cal = Calendario(ano=(2023, 2026))
    cal = Calendario(ano=[2023, 2026])
    df = cal.feriados()
    print(df)
