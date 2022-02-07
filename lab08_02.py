#-----------------------
variaveis = []
#-----------------------

def tipo(rec):
    ope = False
    composta = False
    criar = False
    for elemento in rec:
        try:
            elemento = int(elemento)
        except ValueError:
            if elemento == '+' or elemento == '-':
                pass
            elif elemento == '=':
                criar = True
            elif elemento == 'AND' or elemento == 'OR':
                composta = True
            elif elemento == '==' or elemento == '!=' or elemento == '>=' or elemento == '<=' or elemento == '>' or elemento == '<':
                ope = True
    return ope, composta, criar

def checar(exp):
    resultado = None
    for variavel in variaveis:
        if variavel['Nome'] == exp:
            resultado = int(variavel['valor'])
    if resultado == None:
        return False, exp
    else:
        return resultado

def operacao(rec):
    resultado = None
    try:
        resultado = int(rec[0])
    except ValueError:
        resultado = checar(rec[0])
        if type(resultado) == tuple:
            return resultado
    for i in range(1, len(rec)-1):
        if rec[i] == '+':
            try:
                resultado = resultado + int(rec[i+1])
            except ValueError:
                soma = checar(rec[i+1])
                if type(soma) == tuple:
                    return soma
                else:
                    resultado = resultado + soma

        elif rec[i] == '-':
            try:
                resultado = resultado - int(rec[i+1])
            except ValueError:
                sub = checar(rec[i+1])
                if type(sub) == tuple:
                    return sub
                else:
                    resultado = resultado - sub

    return resultado


def comp(rec):
    cond = False
    for i in range(len(rec)):
        if '==' == rec[i] or '!=' == rec[i] or '>=' == rec[i] or '<=' == rec[i] or '>' == rec[i] or '<' == rec[i] or '>' == rec[i]:
            if type(operacao(rec[0:i])) == tuple:
                return operacao(rec[0:i])
            elif type(operacao(rec[i+1:])) == tuple:
                return operacao(rec[i+1:])
            else:
                if rec[i] == '==':
                    if operacao(rec[0:i]) == operacao(rec[i+1:]):
                        cond = True
                elif rec[i] == '!=':
                    if int(operacao(rec[0:i])) != int(operacao(rec[i+1:])):
                        cond = True

                elif rec[i] == '>=':
                    if int(operacao(rec[0:i])) >= int(operacao(rec[i+1:])):
                        cond = True

                elif rec[i] == '<=':
                    if int(operacao(rec[0:i])) <= int(operacao(rec[i+1:])):
        
                        cond = True
                elif rec[i] == '>':
                    if int(operacao(rec[0:i])) > int(operacao(rec[i+1:])):
                        cond = True
                elif rec[i] == '<':
                    if int(operacao(rec[0:i])) < int(operacao(rec[i+1:])):
                        cond = True
            break
    return cond

def op_composta(exp):
    booleana_geral = []
    exp_refinada = []
    exp_k = 0
    exp_k_f = len(exp)
    for i in range(exp_k_f):
        if exp[i] == 'OR':
            exp_refinada.append(exp[exp_k:i])
            exp_k=i+1
    exp_refinada.append(exp[exp_k:exp_k_f])
    
    for expressoes in exp_refinada:
        booleana = []
        exp_final = []
        k = 0
        k_f = len(expressoes)
        for i in range(k_f):
            if expressoes[i] == 'AND':
                exp_final.append(expressoes[k:i])
                k = i+1
        exp_final.append(expressoes[k:k_f])

        for exp_final_final in exp_final:
            if type(comp(list(exp_final_final))) == tuple:
                return comp(list(exp_final_final))
            else:
                booleana.append(comp(list(exp_final_final)))

        if False in booleana:
            booleana_geral.append(False)
        if True in booleana:
            if 'AND' not in expressoes:
                booleana_geral.append(True)
    
    if True in booleana_geral:
        return True
    elif True not in booleana_geral:
        return False

def testar_var(nome):
  letras = list(nome)
  cond_1 = True
  cond_2 = False
  cond_3 = True
  try:
      letras[0] = int(letras[0])
      cond_1 = False
  except ValueError:
      pass

  for letra in letras:
      try:
          letra = int(letra)
      except ValueError:
          cond_2 = True
    
  cond_3 = oi(letras[1:])

  if cond_1 == True and cond_2 == True and cond_3 == True:
      return True
  else:
      return False

def oi(letras):
  for letra in letras:
    if letra.isalpha() == False and letra.isalnum() == False:
      return False
  return True

def main():
    rec = input().split()
    ope, composta, criar = tipo(rec)
    
    if ope == False and criar == False and composta == False:
        if type(operacao(rec)) == tuple:
            print("Erro de referencia: a variavel {} nao foi definida.".format(operacao(rec)[1]))
        else:

            print(operacao(rec))
    
    if ope == True and composta == False and criar == False:
        cond = comp(rec)
        if cond == True:
            print(1)
        elif cond == False:
            print(0)
        else:
            print("Erro de referencia: a variavel {} nao foi definida.".format(cond))
    if ope == False and composta == False and criar == True:
        resultado = operacao(rec[2:])
        if resultado == False:
            print("Erro de referencia: a variavel {} nao foi definida.".format(operacao(rec)[1]))
        else:
            if testar_var(rec[0]) == 1:
                variaveis.append({'Nome': rec[0], 'valor': resultado})
            else:
                print('Erro de sintaxe: {} nao e um nome permitido para uma variavel.'.format(rec[0]))
    if ope == True and composta == True and criar == False:
        cond = op_composta(rec)
        if cond == True:
            print(1)
        elif cond == False:
            print(0)
        else:
            print("Erro de referencia: a variavel {} nao foi definida.".format(cond[1]))
    if ope == True and composta == True and criar == True:
        #substituir as variaveis, resolver primeiro as expressões simples, as comparações e por fim as compostas
        cond = op_composta(rec[2:])
        if testar_var(rec[0]) != 1:
            print('Erro de sintaxe: {} nao e um nome permitido para uma variavel.'.format(rec[0]))
        
        elif cond == True:
            variaveis.append({'Nome':rec[0], 'valor':1})
            
        elif cond == False:
            variaveis.append({'Nome':rec[0], 'valor':0})
            
        else:
            print("Erro de referencia: a variavel {} nao foi definida.".format(cond[1]))
    if ope == True and composta == False and criar == True:
        cond = comp(rec[2:])
        if testar_var(rec[0]) != 1:
            print('Erro de sintaxe: {} nao e um nome permitido para uma variavel.'.format(rec[0]))
        
        elif cond == True:
            variaveis.append({'Nome':rec[0], 'valor':1})
            
        elif cond == False:
            variaveis.append({'Nome':rec[0], 'valor':0})
            
        else:
            print("Erro de referencia: a variavel {} nao foi definida.".format(cond[1]))
while True:
    try:
        main()
    except EOFError:
        print('Encerrando... Bye-bye.')
        break