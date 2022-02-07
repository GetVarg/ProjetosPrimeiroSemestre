def main():
    while True:
        l_ord = []
        l_abs = []
        rec = input().split()
        if rec == ['0', '0']:
            break
        for n in range(int(rec[0])):
            inp = input().split()
            l_abs.append(inp[0])
            l_ord.append(inp[1])
        l_dist, l_j = (calculo_dist(l_abs, l_ord, int(rec[1])))

        dist_teste = l_dist[0]
        jp = [0]
        for n in range(len(l_dist)):
            if l_dist[n] < dist_teste:
                dist_teste = l_dist[n]
                jp = l_j[n]
        print(jp)

def maior(l_abs, l_ord, k_, i):
    maior_dist = 0
    k = k_
    j = 0
    if len(l_abs) == 2:
        dist_anterior = int(l_abs[k-1])*int(l_abs[k-1]) + (int(l_ord[k-1])-i)*(int(l_ord[k-1])-i)
        dist_atual = int(l_abs[k])*int(l_abs[k]) + (int(l_ord[k])-i)*(int(l_ord[k])-i)
        if dist_atual > dist_anterior:
            return dist_atual, i
        else:
            return dist_anterior, i

    while k+1 < len(l_abs):
            
        dist_atual = int(l_abs[k])*int(l_abs[k]) + (int(l_ord[k])-i)*(int(l_ord[k])-i)
        dist_anterior = int(l_abs[k-1])*int(l_abs[k-1]) + (int(l_ord[k-1])-i)*(int(l_ord[k-1])-i)
        dist_seguinte = int(l_abs[k+1])*int(l_abs[k+1]) + (int(l_ord[k+1])-i)*(int(l_ord[k+1])-i)
  
        if dist_seguinte < dist_atual >= dist_anterior:
            maior_dist =  dist_atual
            j = i
            if i == 87 or i == 90:
                print(dist_atual, dist_anterior, dist_seguinte, maior_dist)
            break
            
        elif dist_atual <= dist_anterior and dist_atual > dist_seguinte:
            if i == 87 or i == 90:
                print('oi', dist_atual, dist_anterior, dist_seguinte)
            k = k - 1

        elif dist_atual > dist_anterior and dist_atual <= dist_seguinte:
            if k + 2 == len(l_abs):
                maior_dist = dist_seguinte
                j = i
                break
            else:
                if i == 87 or i == 90:
                    print('oi1', dist_atual, dist_anterior, dist_seguinte)
                k = k + 1
        elif dist_atual <= dist_seguinte and dist_atual  <= dist_anterior:
            k = k - 1
    return maior_dist, j


def calculo_dist(l_abs, l_ord, y):
    maior_dist = 0
    l_j = []
    l_dist = []
    for i in range(y):
        k = (len(l_abs))//2
        maior_dist, j = maior(l_abs, l_ord, k, i)
        l_dist.append(maior_dist)
        l_j.append(j)
    return l_dist, l_j

main()
'''2 8
-5 6
-6 7
------
3 10
-2 1
-8 7
7 1
--------
2 10
7 4
9 9
--------
3 9
-8 1
-3 3
-6 8
-----
2 6
-3 1
4 3
---------
3 7
-3 3
-1 2
-6 6
3 10
-1 6
-6 9
2 5
2 10
4 9
-2 3
2 8
-2 7
1 3
2 10
10 9
-2 3
3 10
-4 4
-8 2
-9 7
2 5
2 4
1 3
2 9
-3 2
7 8
0 0'''

'''
7
5
9
3
3
6
9
7
5
9
6
4
8
'''