'''
QUESTÃO5. Usando arrays, leia 5 números inteiros exiba-os
ordenados do maior para o menor .'''

tamanho  =  6
controle  =  1
números  = []
enquanto  controle  <  tamanho :
  numero  =  int ( input ( f'Digite o { control } º numero:' ))
  controle  +=  1
  números . anexar ( número )

ordenação  =  ordenado ( números , reverso = Verdadeiro )
print ( f'Números ordenados do maior para o menor: { ordenação } ' )