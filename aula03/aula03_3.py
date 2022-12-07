#perguntar ao usuario um numero de 1 a 10 e declarar o nome da variavel 
num = int(input("adicone um numero: \n"))
#confirmar para o usuario qual numero ele escolheu
print(f"vejo que você escolheu o numero {num}")
#criar um laço onde sai do numero que o usario escolheu até um numero escolhido(15)
while(num <= 15):
    print(num)
    num = num+1
#fazer uma condiçao para caso o numero for menor que 1 ele falar que está longe e se for maior que um prosseguir pro proximo "nivel"
if(num >= 1):
 #saber quantos numeros faltam para cehgar ao 15 e falar para o usuario isso
  numf = num - 15
  print(f"você está há {numf} de distancia do numero final \n")
 #fazer com que o usuario descubra o numero final se for a resposta dele for igual ao 
  resposta = int(input("qual o numero final?"))
  if(resposta == 15):
    print("\nvocê acertou pequeno garfanhoto")