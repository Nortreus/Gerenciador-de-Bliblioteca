import controller.biblioteca_controller as mb
import cursor as cs

class BibliotecaController:
    def __init__(self):
        self._biblioteca = []
        lista = cs.buscar('*','biblioteca')
        for i in lista:
            print(f'{i[1]},{i[2]},{i[3]}')
            self._biblioteca.append(mb.Biblioteca(i[1],i[2],i[3]))
            
        
        
    
        
            
        
    
            
            
            
        
        
        
    