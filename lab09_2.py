def calcular_intersec_len(m, n):
    rows = columns = 0
    for i in m:
        for j in n:
            j = set(j)
            row = [x for x in i if x in j]
            if row != []:
                if columns == 0:
                    columns = len(row)
                rows += 1
    return rows, columns

def calculate_dim(m, n, sum_lens):
    line_intersec, column_intersec = calcular_intersec_len(m, n)
    p = sum_lens - line_intersec
    q = sum_lens - column_intersec

    print(f"{p} x {q}")


while True:
    matrizes = []
    order = input().split()
    sum_lens = int(order[0]) + int(order[1])
    if order == ['0', '0']:
        break
    for j in range(2):
        matriz = list()
        for i in range(int(order[j])):
            recebe = input().split()
            linha = []

            for k in range(int(order[j])):
                linha.append(recebe[k])

            matriz.append(linha)
        matrizes.append(matriz)
    
    m = matrizes[0]

    n = matrizes[1]

    calculate_dim(m, n, sum_lens)