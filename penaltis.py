import random

#Algoritmo de cobrança de penalti

#Atributos do batedor
pont = int(input('Informe o valor de Pontaria: '))
mali = int(input('Informe o valor de Malícia: '))
cat = int(input('Informe o valor de Categoria: '))
especbat = int(input('O batedor é especialista? 5 para Sim e 0 para Não: '))
press = int(input('Informe o valor de 1 a 7 para pressão: '))

dado_chute = random.randint(1,10)

#Atributos do goleiro
reflexo = int(input('Informe o valor de Reflexo do goleiro: '))
mali_go = int(input('Informe o valor de Malícia do goleiro: '))
vel_go = int(input('Informe o valor de Velocidade do goleiro: '))
pulo_go = int(input('Informe o valor de Pulo do goleiro: '))
especgo = int(input('O batedor é especialista? 5 para Sim e 0 para Não: '))
press_go = int(input('Informe a pressão do goleiro de 1 a 7: '))

dado_defesa = random.randint(1,10)

#calcula a média dos atributos, subtrai a pressão e add a carta de espeialista
somachute = pont + mali + cat + dado_chute /4
chute = somachute - press + especbat

acerto = random.randint(1,10)

#calcula a média dos atributos, subtrai a pressão e add a carta de espeialista
somadefesa = reflexo + mali_go + vel_go + pulo_go + dado_defesa /5
defesa = somadefesa + especbat - press_go

#Primeiramente o sistema calcula a dificuldade do chute e imprime encerra caso o batedor erre o chute, senão segue com o desafio entre batedor e goleiro
if chute < acerto:
  print()
  print('Errou!')
  print()
  print('Dado chute:')
  print(dado_chute)
  print('Valor do chute:')
  print(chute)
  print('Dificuldade - O valor do chute tem que ser maior que o acerto')
  print(acerto)
  
#Se o calculo do chute for menor ou igual ao da defesa, o guarda redes defende o chute
elif chute <= defesa:
  print()
  print('Defendeu!')
  print()
  print('Valor do chute: ')
  print(chute)
  print('Valor da defesa: ')
  print(defesa)

#Se os dados do chute forem maiores que os da defesa, o batedor converte a cobrança em gol.
elif chute > defesa:
  print()
  print('Goool!!!')
  print()
  print('Valor do chute: ')
  print(chute)
  print('Valor da defesa: ')
  print(defesa)