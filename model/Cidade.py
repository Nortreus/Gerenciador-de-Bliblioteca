class Cidade:
    _codigo = 0
    def __init__(self,nome, responsavel):
        Cidade._codigo +=1
        self._codigo = Cidade._codigo
        self._nome = nome
        self._blioteca = []
        self._responsavel = responsavel
        