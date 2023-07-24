from model.tema import Tema
import cursor as cs


resultados = cs.buscar("SELECT * FROM gerenciadorbiblioteca.biblioteca;")

# Exibe os resultados
for registro in resultados:
    print(registro)
    
    



