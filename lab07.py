info = input().split(' ')
m = info[0] #1 para codificar e 2 para decodificar
e = int(info[1]) #o número fixo de quantos caracteres codificados devem representar um mesmo caracter original
n = info[2] #quantas linhas a mensagem a ser codificada/decodificada possui

#/////////////////////////////////////////////////////////////
#organizar o codigo recebido
def enumerar(mensagem): #transformar a frase decrptografado em numeros decimais
    letra = []
    mod_msg = list(mensagem)
    for k in range(len(mod_msg)):
        letra.append(ord(mod_msg[k]))
    return letra

def org_codigo(mensagem, e): #organizar o codigo recebido em listas de tamanho 'e', correspondente às letras
    letra = []
    mensagem = list(mensagem)
    for i in range(0, len(mensagem)-e+1, e):
            caracter = mensagem[i:i+e]
            caracter = [''.join(caracter)]
            letra.append(caracter[0])  
    return letra

#/////////////////////////////////////////////////////////////
#CODIFICAÇÃO
def cod_hexa(l): #transformar o codigo de decimal para hexadecimal
    l_cod = []
    for k in range(len(l)):
        l_cod.append(hex(l[k]))
    l_cod = ''.join(l_cod)
    return l_cod

def cod_octadecimal(l): #transformar o codigo de decimal(gerado na função 'enumerar') para hexadecimal
    l_cod = []
    for k in range(len(l)):
        l_cod.append(oct(int(l[k])))
    l_cod = l_cod[::-1]
    l_cod = ''.join(l_cod)
    return l_cod

def limpeza(condição, mensagem):  #chamar as funções correspondentes
    nova_lista=[]
    if condição == 'impar':
        nova_lista = cod_hexa(enumerar(mensagem)).split('0x')
    if condição == 'par':
        nova_lista = cod_octadecimal(enumerar(mensagem)).split('0o')
    
    nova_lista.pop(0)

    for i in range(len(nova_lista)):
        nova_lista[i] = (e-len(nova_lista[i]))*"0"+str(nova_lista[i]).upper()
    return ''.join(nova_lista)

#/////////////////////////////////////////////////////////////
#DECODIFICAÇÃO

def trasnsforma(condição, msg, e): #transformar o codigo de hexa ou octadecimal para decimal
    l = org_codigo(msg, e)
    l_cod = []
    if condição == 'impar':
        for k in range(len(l)):
            n = int(l[k], 16)
            l_cod.append(n)
    if condição == 'par':
        for k in range(len(l)):
            n = int(l[k], 8)
            l_cod.append(n)
        l_cod = l_cod[::-1]
    return l_cod

def decodificação(condição, msg, e):
    l_cod = trasnsforma(condição, msg, e)
    for i in range(len(l_cod)):
        l_cod[i] = chr(int(l_cod[i]))
    l_cod=[''.join(l_cod)]
    return l_cod

#/////////////////////////////////////////////////////////////
#receber as informações/mensagem + chamar as funções
ret = []
msg = []
if m == '1': #quando for para codificar
    for i in range(1, int(n)+1):
        msg.append(input())
        if i%2 != 0:
            ret.append(limpeza('impar', msg[i-1]))
        
        if i%2 == 0:
            ret.append(limpeza('par', msg[i-1]))
            
if m == '2':
    for i in range(1, int(n)+1):
        msg = input()
        if i%2 != 0:
            ret.append(decodificação('impar', msg,e)[0])
        
        if i%2 == 0:
            ret.append(decodificação('par', msg,e)[0])

for k in range(len(ret)):
   print(ret[k])