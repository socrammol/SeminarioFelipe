import csv
'''
imovel_Id;tipoImovel;valorImovel;areaRealPrivativa;latitude;longitude;quartos;banho;suites;vagaGaragem;valorCondominio;valorIptu;Cidade;Regiao;Bairro;Endereco

2576940;Apartamento 1 quarto;179000;41;-19,9219328;-43,9431768;1;1;0;0;500;102;belo-horizonte;centro-sul;Centro;Rua dos Goitacazes, 365
'''
class Reader:
	def __init__(self, path = 'arquivo.csv'):
		self.data = {}
		self.indice = []
		self.tamanho = -1
		
		print("fazendo abrindo arquivo '",path,"'")
		with open(path, 'r') as ficheiro:
			base = []

			ficheiro = csv.reader(ficheiro)
			print('carregando indice de dados')
			for row in ficheiro:
				self.indice = row[0].split(';')
				break
			
			for tipo in self.indice:
				self.data.update({tipo:[]})
			
			print ('carregando dados...')
			for row in ficheiro:
				linha = ''
				for item in row:
					linha = linha + item + '.'
				
				linha = linha[:len(linha)-1]
				base.append(linha)
				items = linha.split(';')

				for i in range(0, len(self.indice)):
					self.data[self.indice[i]].append(items[i])
				
				self.tamanho += 1

		print("Carregamento dos dados concluido. ")
		print("Total inserido: ", len(self.data[self.indice[0]]), "em", len(self.data), "colunas")
		print ("colunas disponíveis são as seqguintes: ")
		print (self.indice)
			
	def getIndices(self):
		return self.indice
	
	def select(self, colums = [], restricao = None):
		return self.__selectColum(self.__selectLines(restricao), colums)

	def __selectLines(self, value =None):
		if value == None:
			return self.data
		else:
			result = {}
			for tipo in self.indice:
				result.update({tipo:[]})
			print('Sekecionando intervalo definido como [', value[0],'] = ', value[1])
			for i in range(0, self.tamanho):
				if self.data[value[0]][i] == value[1]:
					for tipo in self.indice:
						result[tipo].append(self.data[tipo][i])
				
			print('Pronto!', 'Resultados encontradord: ', len(result[self.indice[0]]))
			return result

	def __selectColum(self, data = {}, colums = []):
		tamanho = len(data[self.indice[0]])
		print ('selecionado colunas: ', colums)
		result = []		
		for i in range(0, tamanho):
			print ('data[',colums[0],'][',i,'] = ', data[ colums[0] ][i],'    data[',colums[1],'][',i,'] = ', data[ colums[1] ][i])
			new = [float(data[ colums[0] ][i]) , float(data[ colums[1] ][i])]
			#print('coluna', i, '=', new)
			result.append(new)
		print('Pronto!', 'Resultados encontrados: ', len(result))
		print()
		return result
