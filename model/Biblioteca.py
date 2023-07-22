class Biblioteca:
    def __init__(self,nome, responsavel):
        self._nome = nome
        self._livro = []
        self._responsavel = responsavel
        
    def adicionar_livro(self, livro):
        if livro not in self._livro:
            self._livro.append(livro)
    
    def remover_livro(self, livro):
        if livro in self._livro:
            self._livro.remove(livro)
        
        