import ReaderCSV


rd = ReaderCSV.Reader('imobiliaria_20181026100739.csv')
#rd = ReaderCSV.Reader('teste.csv')

reg = LinearRegressionCIC.Regressao()
#reg.SetAmostras([reader[3,4]])
print()

print('Selecionando dados para amostra 1')
data1 = rd.select(['valorImovel','vagaGaragem'], ['Bairro','Alto Barroca'])

print('Selecionando dados para amostra 2')
data2 = rd.select(['valorImovel','areaRealPrivativa'], ['Bairro','Alto Barroca'])

print('Selecionando dados para amostra 3')
data3 = rd.select(['valorImovel','valorIptu'], ['Bairro','Alto Barroca'])

print('Selecionando dados para amostra 4')
data4 = rd.select(['valorImovel','areaRealPrivativa'])

print()
print()
print('Definindo amostra 1 para análise da regressão.')
reg.SetAmostras(data1)
print('Aplicando regressão na amostra 1....')
valorCalculado = reg.Calcular(5)
print('Concluido!','O resultado é:' ,valorCalculado)

print()
print()
print('Definindo amostra 2 para análise da regressão.')
reg.SetAmostras(data2)
print('Aplicando regressão na amostra 2....')
valorCalculado = reg.Calcular(5)
print('Concluido!','O resultado é:' ,valorCalculado)

print()
print()
print('Definindo amostra 3 para análise da regressão.')
reg.SetAmostras(data3)
print('Aplicando regressão na amostra 3....')
valorCalculado = reg.Calcular(5)
print('Concluido!','O resultado é:' ,valorCalculado)

print()
print()
print('Definindo amostra 4 para análise da regressão.')
reg.SetAmostras(data4)
print('Aplicando regressão na amostra 4....')
valorCalculado = reg.Calcular(5)
print('Concluido!','O resultado é:' ,valorCalculado)
