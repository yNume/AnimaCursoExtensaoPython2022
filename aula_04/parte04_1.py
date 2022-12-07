# primeiro passo: importar  a biblioteca sqllite3 
import sqlite3

#segundo passo:vamos estabelecer uma conexao com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#terceiro passo : criar um objeto do tipo cursor, cursor é onde voce colocará os comandos
cursor = conexao.cursor()

# quarto passo : comando SQL do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#quinto passo : EXECUTAR o comando sql no cursor(sqlLite)
cursor.execute(sql)

#sexto passo: Exibir uma consulta com todos os nomes de heroes e viloes do banco de dados(exibir todas as informaçoes do banco de dados que puxamos o (dc_universe.db)
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)
print("\n para que nos vermos apenas o nome e a classificao \n")
for pessoa in pessoas:
 print(F"Nome:{pessoa[1]} ({pessoa[3]})\n")

print("\n")
#para adicionar um novo heroi ou uma nova informaçao devera voltar para o passo 4 ficará assim:

#quarto.b passo. passo: comando para inserir um herói/vilão
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

cursor.execute(sql)
#desta forma precisamos um comando de confirmaçao 
#sexto passo: confirmar o INSERT com commit() e fechar o banco 
conexao.commit()
conexao.close()