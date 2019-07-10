# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 09:38:02 2019

@author: VINOD
"""
import pandas as pd

pokemonData = pd.read_csv('./pokemon_data.csv')
#print(pokemonData)
#pokemonData.head(5)
a=pokemonData['Name'].unique()
print(a)