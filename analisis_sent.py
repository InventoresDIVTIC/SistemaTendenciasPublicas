import spacy
import pandas as pd

df_claudia='claudia.txt'

frames=[df_claudia]

for colname in frames:
    colname.columns=["message","target"]

for colname in frames:
    print(colname.columns)

