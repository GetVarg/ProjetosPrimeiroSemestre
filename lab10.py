info_suspeito = []
dossie = []
l = []
l_suspeitos = []

def susp(suspeito):
    inp = suspeito.split(':')

    for i in range(2):
        inp[i] = str(inp[i].strip())
    d = dict(inp for i in range(2))
    return d

def igualdade(dossie, l_suspeitos):
    princ_susp = []
    for caracteristica in dossie:
        row = [suspeito for suspeito in l_suspeitos if caracteristica in suspeito]
    for suspeito in row:
        cond = True
        for carac_suspeito in suspeito:
            for carac_dossie in dossie:
                if carac_suspeito.keys() == carac_dossie.keys():
                    if carac_dossie != carac_suspeito:
                        cond = False
        if cond:
            princ_susp.append(suspeito[0]['Nome'])

    return sorted(princ_susp)

while True:
    inp = input().strip()

    if inp == '-':
        l_suspeitos.append(info_suspeito)
        info_suspeito = []
    
    elif inp == '--':
        l_suspeitos.append(info_suspeito)
        rec = input().strip()
        while rec != '---':
            dossie.append(susp(rec))
            rec = input().strip()
        l = igualdade(dossie, l_suspeitos)
        
        if len(l) == 0:
            print("Nenhum suspeito(a) com essas caracteristicas foi identificado(a).")
        
        elif len(l) == 1:
            print("Suspeito(a):")
            print(l[0])
        
        elif len(l)>1:
            print("Suspeitos(as):")
            for nome in l:
                print(nome)
        
        break
        
    else:
        info_suspeito.append(susp(inp))
        