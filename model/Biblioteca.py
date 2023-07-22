class Biblioteca:
    _codigo = 0
    def __init__(self,nome, responsavel):
        Biblioteca._codigo +=1
        self._codigo = Biblioteca._codigo
        self._nome = nome
        self._livro = []
        self._responsavel = responsavel