import LInearRegression
import csv


with open('imobiliaria.csv', 'rb') as ficheiro:
    reader = csv.reader(ficheiro)

reg = LInearRegression.Regressao()
#reg.SetAmostras([reader[3,4]])
reg.SetAmostras([[1,4],[2,5],[3,6],[4,7]])
valorCalculado = reg.Calcular(5)
print(valorCalculado)