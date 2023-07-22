class Usuario:
    _codigo = 0
    def __init__(self,nome,endereço,genero,cpf,livro_empres):
        Usuario._codigo +=1
        self._codigo = Usuario._codigo
        self._nome = nome
        self._endereco = endereço
        self._genero = genero
        self._cpf = cpf
        self._livro_empres = livro_empres
        