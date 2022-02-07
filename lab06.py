class Medalutador:
  def __init__(self, ID, pontos_do_braco_e, pontos_do_braco_d, pontos_do_torso, pontos_das_pernas):
    self.ID = ID
    self.pontos_do_braco_e = pontos_do_braco_e
    self.pontos_do_braco_d = pontos_do_braco_d
    self.pontos_do_torso = pontos_do_torso
    self.pontos_das_pernas = pontos_das_pernas

  def obter_ID(self):
    return self.ID

  def __repr__(self):
     return str(self.ID)


def simular_torneios_de_cyberlutas(lista_de_medalutadores):
  lista_torneio_principal = []
  lista_de_repescagem     = []
  for medalutador in lista_de_medalutadores:
    lista_torneio_principal.append(medalutador)
  while len(lista_torneio_principal) >= 2 or len(lista_de_repescagem) >= 2:
    lista_torneio_principal = aplicar_rodada_de_batalhas(lista_torneio_principal, lista_de_repescagem)
    lista_de_repescagem     = aplicar_rodada_de_batalhas(lista_de_repescagem, None)
  i = lista_torneio_principal.pop(0)
  j = lista_de_repescagem.pop(0)
  print('Cyberluta Final')
  print(f'Medalutadores: {i} vs {j}')
  imprimir_ficha_tecnica(i, j)
  k = batalhar(i, j)
  print(f'Campeao: medalutador {k}')


def aplicar_rodada_de_batalhas(lista_de_medalutadores, lista_de_repescagem):
  if len(lista_de_medalutadores) < 2:
    return lista_de_medalutadores
  lista_de_vencedores = []
  while len(lista_de_medalutadores) >= 2:
    i = lista_de_medalutadores.pop(0) 
    j = lista_de_medalutadores.pop(0)
    if i.obter_ID() > j.obter_ID():
      i, j = j, i
    if lista_de_repescagem != None:
      print('Cyberluta do Torneio Principal')
    else:
      print('Cyberluta da Repescagem')
    print(f'Medalutadores: {i} vs {j}')
    imprimir_ficha_tecnica(i, j)
    k = batalhar(i, j)
    imprimir_resultado_da_batalha(k)
    if lista_de_repescagem != None:
      if i == k:
        lista_de_repescagem.append(j)
      else:
        lista_de_repescagem.append(i)
    lista_de_vencedores.append(k)
  lista_de_vencedores.extend(lista_de_medalutadores)
  return lista_de_vencedores


def imprimir_ficha_tecnica(i, j):
  print(f'\tA{ID} = E{pontos_do_braco_e} + D{pontos_do_braco_d} + {bonus_de_ataque} = {pontos_de_ataque}')
  print(f'\tD{ID} = T{pontos_do_torso} + P{pontos_das_pernas} + {bonus_de_defesa} = {pontos_de_defesa}')
  print(f'\tH{ID} = {habilidade_atual}')

def ficha_tec():
    l1 = []
    l1 = input().split()
    l2 = []
    l2 = input().split()

    t = 0
    e = 0
    d = 0
    p = 0

    for x in range(int(l1[2])):
        l = []
        l = input().split()
        r = dict()
        if l[0]=='T':
            t = t + int(l[1])
        if l[0]=='E':
            e = e + int(l[1])
        if l[0]=='D':
            d = d + int(l[1])
        if l[0]=='P':
            p = p + int(l[1])
        r = {'t': t,'e': e,'d': d,'p': p}
    return r



'''batalhar
Parâmetros: Dois medalutadores i e j que irão batalhar entre si (será explicado mais adiante).
Retorno: O medalutador vencedor da batalha.'''

'''imprimir_ficha_tecnica
Parâmetros: Dois medalutadores i e j.
Retorno: Sem retorno. Deve apenas imprimir a ficha técnica de cada medalutador, no seguinte formato:'''

'''print(f'\tA{ID} = E{pontos_do_braco_e} + D{pontos_do_braco_d} + {bonus_de_ataque} = {pontos_de_ataque}')
print(f'\tD{ID} = T{pontos_do_torso} + P{pontos_das_pernas} + {bonus_de_defesa} = {pontos_de_defesa}')
print(f'\tH{ID} = {habilidade_atual}')'''

'''imprimir_resultado_da_batalha:Parâmetros: Um medalutador k vencedor de uma batalha.
Retorno: Sem retorno. Deve apenas imprimir uma mensagem indicando o vencedor e a sua
medapeça ganha, no formato:'''

'''print(f'Medalutador {k} venceu e recebeu a {tipo_da_medapeca_ganha}{pontos_da_medapeca_ganha}\n')'''