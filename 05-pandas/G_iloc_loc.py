# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:05:03 2019

@author: USRBET
"""

import pandas as pd

path_guardado_bin = "C://Users//USRBET//Documents//GitHub//py-yanez-aguiar-angel-daniel//05-pandas//data//artwork_data_completo.pickle"
df = pd.read_pickle(path_guardado_bin)
df2 = df.set_index('id')

"""
            nota 1      disciplina
pepito      7           5
juanita     8           9
maria       9           2



"""
data={"Nota 1":{"Pepito":7,"Juanita":8,"Maria":9},"Disciplina":{"Pepito":5,"Juanita":9,"Maria":2}}
df3 = pd.DataFrame(data)

primero = df2.loc[1035]
segundo = df2.iloc[1035]

df3.loc["Pepito","Disciplina"]
df3.loc["Pepito",["Disciplina","Nota 1"]]
df3.loc[["Pepito","Juanita"]]

df3.loc[["Pepito","Juanita"],["Nota 1"]]
df3.loc[["Pepito","Juanita"],"Nota 1"]

df3.loc[[True,False,True]]

condicion_nota = df3["Nota 1"] > 7
condicion_disc = df3["Disciplina"] > 7

mayores_siete = df3.loc[condicion_nota][condicion_disc]

df3.loc["Maria","Disciplina"]=7

condicion_disc_menor = df3["Disciplina"] < 7
df3.loc[condicion_disc_menor,"Disciplina"]=7

df3.loc["Pepito",:] = 10

df3.loc[:,"Disciplina"] = 7

promedio = (df3.loc[:,"Disciplina"] + df3.loc[:,"Nota 1"])/2
df3["Promedio"]=promedio