from sys import displayhook
import pandas as pd


contatos = pd.read_excel("./enviar.xlsx")
displayhook(contatos)

