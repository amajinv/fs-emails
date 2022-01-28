#TODO inicializar clases y métodos 
#TODO calculos de información 
import pandas as pd
from datetime import date, timedelta

class FS():

    f3_name ='220119-0827-f3-output'
    f3 = pd.read_csv(f'input_planillas/{f3_name}.csv', sep=';')
    fecha_inicial_reserva = '01-01-2021'

    def __init__(self) -> None:
        self.set_fecha_reserva() # Arreglar fecha reserva por conflicto de idioma
        self.filter_per_year_and_state()
        self.add_month_col()
        self.classify_90_days()

    def set_fecha_reserva(self):
        self.f3["fecha_reserva"] = self.f3["fecha_reserva"].replace(["ene", "abr", "ago", "dic"], ["jan", "apr", "aug", "dec"], regex=True)  # cambio idioma mes
        self.f3["fecha_reserva"] = pd.to_datetime(self.f3["fecha_reserva"], format='%d-%b-%Y')  # cambio de tipo de dato   

    def filter_per_year_and_state(self):
        self.f3 = self.f3.loc[(self.f3['fecha_reserva'] > self.fecha_inicial_reserva) & (self.f3['descripcion6']=='enviado') | (self.f3['descripcion6']=='reservado')].reset_index(drop=True)

    def add_month_col(self): 
        self.f3['mes']  = self.f3["fecha_reserva"].dt.strftime('%b-%y')

    def classify_90_days(self):
        fecha_vencimiento = date.today() - timedelta(days=90)
        self.f3.loc[self.f3["fecha_reserva"] < pd.to_datetime(fecha_vencimiento), 'val_dias'] = 'Mayor a 90 días'
        self.f3.loc[self.f3["fecha_reserva"] >= pd.to_datetime(fecha_vencimiento), 'val_dias'] = self.f3.loc[self.f3["fecha_reserva"] >= pd.to_datetime(fecha_vencimiento), 'mes'].valuestabla_html = open("fig.html", "r").read()

    def calculos(self):
        x_90_dias = self.f3.groupby(['Mes', "val_dias"], sort=False)['cant*costoprmd'].sum().reset_index()
        x_90_dias["color"] = x_90_dias["val_dias"]
        x_90_dias.loc[x_90_dias["val_dias"] != "Mayor a 90 días" , "color" ] = "Menor a 90 días"
        x_90_dias["cant*costoprmd"]=round((x_90_dias["cant*costoprmd"]/1e6),2)

def call_fs():
    pass

if __name__=='__main__':
    call_fs()