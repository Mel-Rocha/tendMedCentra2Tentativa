dados = []

#<leituraTxt>
file = open('arquivo.txt', 'r')
dados_car_esp = file.readlines()
file.seek(0)
file.close



for i in dados_car_esp:
  dados.append(float(i.rstrip()))

  
#print(dados)

dados.sort()
print(dados)

#</leituraTxt>
#<orgGeral>
soma_lista = sum(dados)



#<paORim>
dados_len = len(dados)
if (dados_len % 2) == 0:
  MEDIANA_v = (dados[int(dados_len / 2)] + dados[int((dados_len / 2) - 1)]) / 2
  Q1_v = dados[int((dados_len / 4))]
 

else:
  MEDIANA_v = dados[int((dados_len / 2))]
  Q1_v = (dados[int(dados_len / 4)] + dados[int((dados_len / 4) - 1)]) / 2

  
print(f'MEDIANA: {MEDIANA_v:.2f}')
print(f'Q1: {Q1_v:.2f}')
#print(f'Q3: {Q3_v}')
'''
Ta errado os q
'''


#</paORim>



  
#<orgGeral>
 
#<calc>

#<media>
MEDIA_v = soma_lista / dados_len
print(f'MÉDIA: {MEDIA_v:.2f}')
#</media>

#<maiorMenor>

MENOR_v = dados[0]
MAIOR_v = dados[-1]
AMPLITUDE_v = MAIOR_v - MENOR_v
print(f'MAIOR: {dados[-1]:.2f}')
print(f'MENOR: {dados[0]:.2f}')
print(f'AMPLITUDE: {AMPLITUDE_v}')

#</maiorMenor>

