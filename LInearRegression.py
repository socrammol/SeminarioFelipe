class Regressao:
    def __init__(self):
        self._amostras = []
        self._nAmostras = 0
        self._somaX = 0
        self._somaY = 0,
        self._somaX2 = 0
        self._somaXvY = 0
        self._somaXvX = 0
        self._declive = 0
        self._intercepto = 0

    def SetAmostras(self, amostras):
        if type(amostras) != list:
            print ('amostras invalidas')
        else:
            self._amostras = amostras
            self._Preparar()

    def _Preparar(self):
        self._nAmostras = len(self._amostras)
        self._somaX = sum([x[0] for x in self._amostras])
        self._somaY = sum([x[1] for x in self._amostras])
        self._somaXvY = sum([x[0] * x[1] for x in self._amostras])
        self._somaXvX = sum([x[0] ** 2 for x in self._amostras])
        self._declive = ((self._nAmostras * self._somaXvY) - (self._somaX*self._somaY)) / ((self._nAmostras * self._somaXvX) - (self._somaX ** 2))
        self._intercepto = (self._somaY - self._declive*self._somaX) / self._nAmostras



    def Calcular(self, valor):
        return self._intercepto + (self._declive * valor)


"""import LInearRegression

reg = Regressao()
reg.SetAmostras([[1,4],[2,5],[3,6],[4,7]])
valorCalculado = reg.Calcular(5)
print(valorCalculado)"""