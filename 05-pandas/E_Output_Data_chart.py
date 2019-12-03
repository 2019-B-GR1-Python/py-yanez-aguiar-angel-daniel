# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 08:46:27 2019

@author: USRBET
"""
import xlsxwriter
import os
import pandas as pd
import numpy as np
import sqlite3

path_guardado_bin = "C://Users//USRBET//Documents//GitHub//py-yanez-aguiar-angel-daniel//05-pandas//data//artwork_data_completo.pickle"
df5 = pd.read_pickle(path_guardado_bin)
num_artistas = df5['artist'].value_counts()


workbook = xlsxwriter.Workbook('chart_line.xlsx')
worksheet = workbook.add_worksheet()

# Add the worksheet data to be plotted.
data = [10, 40, 50, 20, 10, 50]
worksheet.write_column('A1', num_artistas)

# Create a new chart object.
chart = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
chart.add_series({'values': '=Sheet1!$A$1:$A$6'})
#chart.add_series({'values': '=Sheet1!$A$1:$A${}'.format(len(num_artistas.index)+1)})

# Insert the chart into the worksheet.
worksheet.insert_chart('C1', chart)

workbook.close()
