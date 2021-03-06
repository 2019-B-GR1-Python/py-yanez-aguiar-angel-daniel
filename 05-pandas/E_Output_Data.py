# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:57:47 2019

@author: USRBET
"""

import os
import pandas as pd
import numpy as np
import sqlite3
import xlsxwriter
path_guardado_bin = "C://Users//USRBET//Documents//GitHub//py-yanez-aguiar-angel-daniel//05-pandas//data//artwork_data_completo.pickle"
df5 = pd.read_pickle(path_guardado_bin)
df = df5.iloc[49980:50019,:].copy()
# tipos archivos
# JSON
# EXCEL
# SQL

### EXCEL ###
path_guardado = "C://Users//USRBET//Documents//GitHub//py-yanez-aguiar-angel-daniel//05-pandas//data//mi_df_completo.xlsx"
df.to_excel(path_guardado,index=False)
columnas = ['artist','title','year']
df.to_excel(path_guardado, columns=columnas)
### multiples hojas de trabajo ###
path_multiple = "C://Users//USRBET//Documents//GitHub//py-yanez-aguiar-angel-daniel//05-pandas//data//mi_df_multiple.xlsx"
writer = pd.ExcelWriter(path_multiple, engine='xlsxwriter')
df.to_excel(writer,sheet_name = 'Primera')
df.to_excel(writer,sheet_name = 'Segunda',index=True)
df.to_excel(writer,sheet_name = 'Tercera',columns=columnas)
writer.save()

num_artistas = df['artist'].value_counts()
path_colores = "C://Users//USRBET//Documents//GitHub//py-yanez-aguiar-angel-daniel//05-pandas//data//mi_df_colores.xlsx"
writer = pd.ExcelWriter(path_colores, engine='xlsxwriter')
num_artistas.to_excel(writer, sheet_name='Artistas')

hoja_artistas = writer.sheets['Artistas']

rango_celdas = 'B2:B{}'.format(len(num_artistas.index)+1)

formato_artistas = {"type":"2_color_scale",
                    "min_value":"10",
                    "min_type":"persentile",
                    "max_value":"99",
                    "max_type":"percentile"}
hoja_artistas.conditional_format(rango_celdas,formato_artistas)

writer.save()

workbook = xlsxwriter.Workbook('C://Users//USRBET//Documents//GitHub//py-yanez-aguiar-angel-daniel//05-pandas//data//mi_df_colores.xlsx')
worksheet = workbook.add_worksheet()
data = num_artistas.values
worksheet.write_column('B2',data)
chart = workbook.add_chart({'type':'line'})
chart.add_series({'values':'=Sheet1!$B$2:$B$4'})
worksheet.insert_chart('C1', chart)
workbook.close()

######## SQL ##########

with sqlite3.connect("C://Users//USRBET//Documents//GitHub//py-yanez-aguiar-angel-daniel//05-pandas//data//bdd_artist.db") as conexion:
    df5.to_sql('py_artistas',conexion)
    
####### JSON #########
df.to_json('C://Users//USRBET//Documents//GitHub//py-yanez-aguiar-angel-daniel//05-pandas//data//artist.json')

df.to_json('C://Users//USRBET//Documents//GitHub//py-yanez-aguiar-angel-daniel//05-pandas//data//artist_table.json', orient='table')
