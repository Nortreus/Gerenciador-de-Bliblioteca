class Livro:
    
    def __init__(self, titulo, autor,ano_publicacao,num_copias,tema):
        
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._num_copias = num_copias
        self._tema = tema
            
        
    def emprestar(self):
        if self._num_copias >= 0:
            self._num_copias -= 1
            return True
        return False
        
    def devolver(self): 
        self._num_copias += 1
        
   