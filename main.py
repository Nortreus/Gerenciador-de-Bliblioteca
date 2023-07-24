from model.tema import Tema
import controller.biblioteca_controller as cb
import cursor as cs


resultados = cs.buscar('*',tabela = 'biblioteca')

# Exibe os resultados
for registro in resultados:
    print(registro)
    
cb.BibliotecaController()
    



