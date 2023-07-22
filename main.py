from model.tema import Tema
from cursor import conexao

cursor = conexao()

print(cursor.is_connected())