#o comando imput serve para o usuario interagir com a  plataforma, para guardar a informação ou seja para recerber uma entrada
"print é uma saida ou seja o usuario nao coloca nada"
#para escrever um numero inteiro é necessario colocar o int(input(...)) para que o programa reconheça que a "idade" na verdade é um numero inteiro assim podemos dobrar ele
"para colocar um espaçõ na area do usuario você deve por o \n dentro dos pareteses da açao"
#print("\n escreva seu nome"). Desta forma pulará uma linha antes da frasse
#print("escreva seu nome\n"). desta forma pulará uma linha depois da frase
"somente oq estiver identado(identado é tudo aqui que estiver ligado a algo neste caso é o que esta recuado para direita na linha 43) será condicionado ao if"
#o else serve para o "se nao" logo poderemos dizer que o else é o inverso do if 


"vamos começar o codigo"




#para saber o nome e o sobrenome do usuario
print("Olá como vai para melhor apresentaçao poderia me dizer seu nome?\n ")
nome = input("\n digite seu nome: ")

Sobrenome = input("\n digite o seu sobrenome: ")

#para exibir que o sistema reconheceu  o nome

print(f"\n Olá senhor {nome} meu nome é Celiús prazer, eu gostaria e eu tenho 1945 anos de idade. e você?")

#para saber a idade do usuario


idade = int(input("\n Qual a sua idade? "))

#para exibir um comunicado com o usario

print(f" \n olha eu até lembro da epoca que eu tinha {idade} anos de idade o mundo era totalmente diferente \n")

dobro = idade * 2

print(f"voce sabia que o dobro da sua idade é{dobro} \n ")

print(f"por favor {nome} digite se você for do genero Masculino M, se for Feminino F")
genero = input("digite M ou F: ")
#para colocarmos um idicador de condicional o "SE" nos utilizaremos o (if)

#se o usuario for maior de idade mostre"voce é maior de idade já pode dirigir e beber


if idade >= 18:
  print(f"\n mas tome cuidado viu? pois com {idade} é uma idade de ouro onde voce pensa que tem varios poderes porem com grandes podores vem grandes resposabilidades está me escutando {nome} ? \n")
else:
  print("\n você é jovem ainda")

if idade >= 18 and genero == "M":
  print("\n Voce ja se alistou soube que é obrigatoriou se nao voce irá ter que prestar o serviço militar obrigatorio")
#para terminar uma condiçao "if" ou o "else" temos que finalizar a açao com o dois pontos : para sinalizar que a setença terminou

