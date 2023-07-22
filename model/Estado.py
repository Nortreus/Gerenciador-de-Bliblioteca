class Estado:
    _codigo = 0
    def __init__(self,nome,cidade,responsavel):
        Estado._codigo +=1
        self._codigo = Estado._codigo
        self._nome = nome
        self._cidade = cidade
        self._responsavel = responsavel