from datetime import date, datetime, timedelta


class DatasBR:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata()

    def mes_cadastro(self):
        meses_ano = [
            'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
            'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
        ]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_ano[mes_cadastro]

    def dia_semana(self):
        dias_semana = [
            'segunda', 'terça', 'quarta', 'quinta',
            'sexta','sábado', 'domingo'
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dias_semana[dia_semana]

    def formata(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        """ timedelta +30 apenas para simular ja q classe de ex. sempre pegara datahora atual """
        tempo_fake = datetime.today() + timedelta(days=30)
        tempo_cadastro = tempo_fake - self.momento_cadastro
        return tempo_cadastro.days