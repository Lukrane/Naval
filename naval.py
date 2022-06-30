colunas = 20
linhas = 20
matriz = [0] * colunas
matriz2 = [0] * colunas
matriz3 = [0] * colunas
loop = 0
fragatas = 5
cruzador = 4
portaavioes = 3
escolhaL = 0
escolhaL2 = 0
escolhaC = 0
escolhaC2 = 0
condicao = [0] * colunas
condicao2 = [0] * colunas
pontuacao = 0
fimloop = 0
print('Este é um simulador de batalha naval, onde um jogador posiciona suas 
embarcações e o outro tenta encontra-lás')
print('O Jogador 1 escolhe as posições através de um numero representando a linha 
da parte, e um segundo numero representando a respectiva coluna)')
for cont in range(colunas):
    matriz[cont] = [0] * linhas
    print(matriz[0])
for cont in range(colunas ):
    condicao[cont] = [0] * linhas
for cont in range(colunas ):
    condicao2[cont] = [0] * linhas
for cont in range(colunas):
    matriz2[cont] = [0] * linhas
for cont in range(colunas):
    matriz3[cont] = [0] * linhas
print('Fragatas: 2 partes alinhadas verticalmente ou horizontalmente')
for cont in range(fragatas):
    loop += 1
    while loop == 1:
        print('Fragata', cont + 1)
        escolhaL = int(input('insira a linha da primeira parte de 1 até 20'), )
        escolhaL -= 1
        escolhaC = int(input('insira a coluna da primeira parte, de 1 até 20'), )
        escolhaC -= 1
        while matriz[escolhaL][escolhaC] == 1:
            print('Número inválido, insira novamente um número que não esta ocupado
ao escolhido')
            escolhaL = int(input('insira a linha da primeira parte, de 1 até 
20'), )
            escolhaL -= 1
            escolhaC = int(input('insira a coluna da primeira parte, de 1 até 20'),
)
            escolhaC -= 1
        escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 20'), )
        escolhaL2 -= 1
        while escolhaL2 != (escolhaL - 1) and escolhaL2 != (escolhaL + 1) and 
escolhaL2 != escolhaL:
            print('Número inválido, insira novamente um número adjacente ao 
escolhido')
            escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 
20'), )
            escolhaL2 -= 1
        escolhaC2 = int(input('insira a coluna da segunda parte, de 1 até 20'), )
        escolhaC2 -= 1
        while escolhaC2 != (escolhaC - 1) and escolhaC2 != (escolhaC + 1) and 
escolhaC2 != escolhaC or escolhaC2 != escolhaC and escolhaL2 != escolhaL or 
escolhaC2 == escolhaC and escolhaL2 == escolhaL:
            print('Número inválido, insira novamente um número adjacente ao 
escolhido')
            escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 
20'), )
            escolhaL2 -= 1
            escolhaC2 = int(input('coluna da segunda parte, de 1 até 20'), )
            escolhaC2 -= 1
        while matriz[escolhaL2][escolhaC2] == 1:
            print('Número inválido, insira novamente um número que não esta ocupado
ao escolhido')
            escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 
20'), )
            escolhaL2 -= 1
            escolhaC2 = int(input('insira a coluna da segunda parte, de 1 até 20'),
)
            escolhaC2 -= 1
            while escolhaL2 != (escolhaL - 1) and escolhaL2 != (escolhaL + 1) and 
escolhaL2 != escolhaL or escolhaC2 != (escolhaC - 1) and escolhaC2 != (escolhaC + 
1) and escolhaC2 != escolhaC or escolhaC2 != escolhaC and escolhaL2 != escolhaL:
                print('Número inválido, insira novamente um número adjacente ao 
escolhido')
                escolhaC2 = int(input('insira a coluna da segunda parte, de 1 até 
20'), )
                escolhaC2 -= 1
        for cont2 in range(linhas):
            if escolhaL == cont2:
                for cont3 in range(colunas):
                    if escolhaC == cont3:
                        matriz[cont2][cont3] += 1
            if escolhaL2 == cont2:
                for cont4 in range(colunas):
                    if escolhaC2 == cont4:
                        matriz[cont2][cont4] += 1
        for cont2 in range(linhas):
            if escolhaL == cont2:
                for cont3 in range(colunas):
                    if escolhaC == cont3:
                        matriz3[cont2][cont3] += (cont + 1)
            if escolhaL2 == cont2:
                for cont4 in range(colunas):
                    if escolhaC2 == cont4:
                        matriz3[cont2][cont4] += (cont + 1)
        for cont2 in range(linhas):
            print(matriz[cont2])
        loop -= 1
print('o cruzador possui três peças alinhadas verticalmente ou horizontalmente')
for cont in range(cruzador):
    loop += 1
    while loop == 1:
        print('Cruzador', cont + 1)
        escolhaL = int(input('insira a linha da primeira parte de 1 até 20'), )
        escolhaL -= 1
        escolhaC = int(input('insira a coluna da primeira parte, de 1 até 20'), )
        escolhaC -= 1
        while matriz[escolhaL][escolhaC] == 1:
            print('Número inválido, insira novamente um número que não esta ocupado
ao escolhido')
            escolhaL = int(input('insira a linha da primeira parte, de 1 até 
20'), )
            escolhaL -= 1
            escolhaC = int(input('insira a coluna da primeira parte, de 1 até 20'),
)
            escolhaC -= 1
        escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 20'), )
        escolhaL2 -= 1
        while escolhaL2 != (escolhaL - 1) and escolhaL2 != (escolhaL + 1) and 
escolhaL2 != escolhaL:
            print('Número inválido, insira novamente um número adjacente ao 
escolhido')
            escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 
20'), )
            escolhaL2 -= 1
        escolhaC2 = int(input('insira a coluna da segunda parte, de 1 até 20'), )
        escolhaC2 -= 1
        while escolhaC2 != (escolhaC - 1) and escolhaC2 != (escolhaC + 1) and 
escolhaC2 != escolhaC or escolhaC2 != escolhaC and escolhaL2 != escolhaL or 
escolhaL2 == escolhaL and escolhaC2 == escolhaC:
            print('Número inválido, insira novamente um número adjacente ao 
escolhido')
            escolhaC2 = int(input('insira a coluna da segunda parte, de 1 até 20'),
)
            escolhaC2 -= 1
        while matriz[escolhaL2][escolhaC2] == 1:
            print('Número inválido, insira novamente um número que não esta ocupado
OU escolhido')
            escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 
20'), )
            escolhaL2 -= 1
            escolhaC2 = int(input('insira a coluna da segunda parte, de 1 até 20'),
)
            escolhaC2 -= 1
            while escolhaL2 != (escolhaL - 1) and escolhaL2 != (escolhaL + 1) and 
escolhaL2 != escolhaL or escolhaC2 != (escolhaC - 1) and escolhaC2 != (escolhaC + 
1) and escolhaC2 != escolhaC or escolhaC2 != escolhaC and escolhaL2 != escolhaL or 
escolhaL2 == escolhaL and escolhaC2 == escolhaC:
                print('Número inválido, insira novamente um número adjacente OU 
escolhido')
                escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 
20'), )
                escolhaL2 -= 1
                escolhaC2 = int(input('insira a coluna da segunda parte, de 1 até 
20'), )
                escolhaC2 -= 1
        while escolhaC2 < escolhaC and escolhaL2 == escolhaL and (escolhaC - 2) < 0
or escolhaL2 < escolhaL and escolhaC2 == escolhaC and (escolhaL - 2) < 0 or 
escolhaC2 > escolhaC and escolhaL2 == escolhaL and (escolhaC + 3) > num or 
escolhaL2 > escolhaL and escolhaC2 == escolhaC and (escolhaL + 3) > num:
            print('escolha invalida; posição ultrapassa a borda do campo')
            escolhaL = int(input('insira a linha da primeira parte, de 1 até 
20'), )
            escolhaL -= 1
            escolhaC = int(input('insira a coluna da primeira parte, de 1 até 20'),
)
            escolhaC -= 1
            while matriz[escolhaL][escolhaC] == 1:
                print('Número inválido, insira novamente um número que não esta 
ocupado ao escolhido')
                escolhaL = int(input('insira a linha da primeira parte, de 1 até 
20'), )
                escolhaL -= 1
                escolhaC = int(input('insira a coluna da primeira parte, de 1 até 
20'), )
                escolhaC -= 1
                while escolhaL2 != (escolhaL - 1) and escolhaL2 != (
                        escolhaL + 1) and escolhaL2 != escolhaL or escolhaC2 != 
(escolhaC - 1) and escolhaC2 != (
                        escolhaC + 1) and escolhaC2 != escolhaC or escolhaC2 != 
escolhaC and escolhaL2 != escolhaL or escolhaL2 == escolhaL and escolhaC2 == 
escolhaC:
                    print('Número inválido, insira novamente um número adjacente OU
escolhido')
                    escolhaL2 = int(input('insira a linha da segunda parte, de 1 
até 20'), )
                    escolhaL2 -= 1
                    escolhaC2 = int(input('insira a coluna da segunda parte, de 1 
até 20'), )
                    escolhaC2 -= 1
            while escolhaL2 != (escolhaL - 1) and escolhaL2 != (escolhaL + 1) and 
escolhaL2 != escolhaL or escolhaC2 != (escolhaC - 1) and escolhaC2 != (escolhaC + 
1) and escolhaC2 != escolhaC or escolhaC2 != escolhaC and escolhaL2 != escolhaL or 
escolhaL2 == escolhaL and escolhaC2 == escolhaC:
                print('Número inválido, insira novamente um número adjacente OU 
escolhido')
                escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 
20'), )
                escolhaL2 -= 1
                escolhaC2 = int(input('insira a coluna da segunda parte, de 1 até 
20'), )
                escolhaC2 -= 1
                while matriz[escolhaL][escolhaC] == 1:
                    print('Número inválido, insira novamente um número que não esta
ocupado ao escolhido')
                    escolhaL = int(input('insira a linha da primeira parte, de 1 
até 20'), )
                    escolhaL -= 1
                    escolhaC = int(input('insira a coluna da primeira parte, de 1 
até 20'), )
                    escolhaC -= 1
            escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 
20'), )
            escolhaL2 -= 1
            escolhaC2 = int(input('insira a coluna da segunda parte, de 1 até 20'),
)
            escolhaC2 -= 1
            while matriz[escolhaL2][escolhaC2] == 1:
                print('Número inválido, insira novamente um número que não esta 
ocupado OU escolhido')
                escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 
20'), )
                escolhaL2 -= 1
                escolhaC2 = int(input('insira a coluna da segunda parte, de 1 até 
20'), )
                escolhaC2 -= 1
                while escolhaL2 != (escolhaL - 1) and escolhaL2 != (escolhaL + 1) 
and escolhaL2 != escolhaL or escolhaC2 != (escolhaC - 1) and escolhaC2 != (escolhaC
+ 1) and escolhaC2 != escolhaC or escolhaC2 != escolhaC and escolhaL2 != escolhaL 
or escolhaL2 == escolhaL and escolhaC2 == escolhaC:
                    print('Número inválido, insira novamente um número adjacente OU
escolhido')
                    escolhaL2 = int(input('insira a linha da segunda parte, de 1 
até 20'), )
                    escolhaL2 -= 1
                    escolhaC2 = int(input('insira a coluna da segunda parte, de 1 
até 20'), )
                    escolhaC2 -= 1
            while escolhaL2 != (escolhaL - 1) and escolhaL2 != (escolhaL + 1) and 
escolhaL2 != escolhaL or escolhaC2 != (escolhaC - 1) and escolhaC2 != (escolhaC + 
1) and escolhaC2 != escolhaC or escolhaC2 != escolhaC and escolhaL2 != escolhaL or 
escolhaL2 == escolhaL and escolhaC2 == escolhaC:
                print('Número inválido, insira novamente um número adjacente OU 
escolhido')
                escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 
20'), )
                escolhaL2 -= 1
                escolhaC2 = int(input('insira a coluna da segunda parte, de 1 até 
20'), )
                escolhaC2 -= 1
                while matriz[escolhaL2][escolhaC2] == 1:
                    print('Número inválido, insira novamente um número que não esta
ocupado OU escolhido')
                    escolhaL2 = int(input('insira a linha da segunda parte, de 1 
até 20'), )
                    escolhaL2 -= 1
                    escolhaC2 = int(input('insira a coluna da segunda parte, de 1 
até 20'), )
                    escolhaC2 -= 1
        if escolhaC2 == escolhaC and (escolhaL + 3) > num and escolhaL2 > escolhaL 
or escolhaL2 == escolhaL and (escolhaC + 3) > num and escolhaC2 > escolhaC or 
escolhaL2 == escolhaL and (escolhaC - 2) < 0 and escolhaC2 < escolhaC or escolhaC2 
== escolhaC and (escolhaL - 2) < 0 and escolhaL2 < escolhaL:
            if escolhaC2 == escolhaC and matriz[(escolhaL + 2)][escolhaC2] == 1 and
escolhaL2 > escolhaL:
                print('posição inválida pois a terceira parte esta ocupada; observe
o campo e escolha um lugar com espaço para 3 partes alinhadas')
            elif escolhaL2 == escolhaL and matriz[escolhaL2][escolhaC + 2] == 1 and
escolhaC2 > escolhaC:
                print('posição inválida pois a terceira parte esta ocupada; observe
o campo e escolha um lugar com espaço para 3 partes alinhadas')
            elif escolhaC2 == escolhaC and matriz[(escolhaL - 2)][escolhaC2] == 1 
and escolhaL2 < escolhaL:
                print('posição inválida pois a terceira parte esta ocupada; observe
o campo e escolha um lugar com espaço para 3 partes alinhadas')
            elif escolhaL2 == escolhaL and matriz[escolhaL2][escolhaC - 2] == 1 and
escolhaC2 < escolhaC:
                print('posição inválida pois a terceira parte esta ocupada; observe
o campo e escolha um lugar com espaço para 3 partes alinhadas')
        else:
            loop -= 1
    for cont2 in range(linhas):
        if escolhaL == cont2:
            for cont3 in range(colunas):
                if escolhaC == cont3:
                    matriz[cont2][cont3] += 1
        if escolhaL2 == cont2:
            for cont4 in range(colunas):
                if escolhaC2 == cont4:
                    matriz[cont2][cont4] += 1
    for cont2 in range(linhas):
        if escolhaL == cont2:
            for cont3 in range(colunas):
                if escolhaC == cont3:
                    matriz3[cont2][cont3] += (cont + 6)
        if escolhaL2 == cont2:
            for cont4 in range(colunas):
                if escolhaC2 == cont4:
                    matriz3[cont2][cont4] += (cont + 6)
    if escolhaL == escolhaL2 and escolhaC2 > escolhaC:
        matriz[escolhaL][(escolhaC + 2)] += 1
    elif escolhaC == escolhaC2 and escolhaL2 > escolhaL:
        matriz[(escolhaL + 2)][escolhaC] += 1
    elif escolhaC == escolhaC2 and escolhaL2 < escolhaL:
        matriz[(escolhaL - 2)][escolhaC] += 1
    elif escolhaL == escolhaL2 and escolhaC2 < escolhaC:
        matriz[escolhaL][escolhaC - 2] += 1
    if escolhaL == escolhaL2 and escolhaC2 > escolhaC:
        matriz3[escolhaL][(escolhaC + 2)] += (cont + 6)
    elif escolhaC == escolhaC2 and escolhaL2 > escolhaL:
        matriz3[(escolhaL + 2)][escolhaC] += (cont + 6)
    elif escolhaC == escolhaC2 and escolhaL2 < escolhaL:
        matriz3[(escolhaL - 2)][escolhaC] += (cont + 6)
    elif escolhaL == escolhaL2 and escolhaC2 < escolhaC:
        matriz3[escolhaL][(escolhaC - 2)] += (cont + 6)
    for cont2 in range(linhas):
        print(matriz[cont2])
print('o porta-avioes possui quatro peças alinhadas verticalmente ou 
horizontalmente')
for cont in range(portaavioes):
    loop += 1
    while loop == 1:
        print('porta-avioes', cont + 1)
        escolhaL = int(input('insira a linha da primeira parte de 1 até 20'), )
        escolhaL -= 1
        escolhaC = int(input('insira a coluna da primeira parte, de 1 até 20'), )
        escolhaC -= 1
        while matriz[escolhaL][escolhaC] == 1:
            print('Número inválido, insira novamente um número que não esta ocupado
ao escolhido')
            escolhaL = int(input('insira a linha da primeira parte, de 1 até 
20'), )
            escolhaL -= 1
            escolhaC = int(input('insira a coluna da primeira parte, de 1 até 20'),
)
            escolhaC -= 1
        escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 20'), )
        escolhaL2 -= 1
        while escolhaL2 != (escolhaL - 1) and escolhaL2 != (escolhaL + 1) and 
escolhaL2 != escolhaL:
            print('Número inválido, insira novamente um número adjacente ao 
escolhido')
            escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 
20'), )
            escolhaL2 -= 1
        escolhaC2 = int(input('insira a coluna da segunda parte, de 1 até 20'), )
        escolhaC2 -= 1
        while escolhaC2 != (escolhaC - 1) and escolhaC2 != (
                escolhaC + 1) and escolhaC2 != escolhaC or escolhaC2 != escolhaC 
and escolhaL2 != escolhaL:
            print('Número inválido, insira novamente um número adjacente ao 
escolhido')
            escolhaC2 = int(input('insira a coluna da primeira parte, de 1 até 
20'), )
            escolhaC2 -= 1
        while matriz[escolhaL2][escolhaC2] == 1:
            print('Número inválido, insira novamente um número que não esta ocupado
OU escolhido')
            escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 
20'), )
            escolhaL2 -= 1
            escolhaC2 = int(input('insira a coluna da segunda parte, de 1 até 20'),
)
            escolhaC2 -= 1
            while escolhaL2 != (escolhaL - 1) and escolhaL2 != (
                    escolhaL + 1) and escolhaL2 != escolhaL or escolhaC2 != 
(escolhaC - 1) and escolhaC2 != (
                    escolhaC + 1) and escolhaC2 != escolhaC or escolhaC2 != 
escolhaC and escolhaL2 != escolhaL or escolhaL2 == escolhaL and escolhaC2 == 
escolhaC:
                print('Número inválido, insira novamente um número adjacente OU 
escolhido')
                escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 
20'), )
                escolhaL2 -= 1
                escolhaC2 = int(input('insira a coluna da segunda parte, de 1 até 
20'), )
                escolhaC2 -= 1
        while escolhaL2 != (escolhaL - 1) and escolhaL2 != (
                escolhaL + 1) and escolhaL2 != escolhaL or escolhaC2 != (escolhaC -
1) and escolhaC2 != (
                escolhaC + 1) and escolhaC2 != escolhaC or escolhaC2 != escolhaC 
and escolhaL2 != escolhaL or escolhaL2 == escolhaL and escolhaC2 == escolhaC:
            print('Número inválido, insira novamente um número adjacente OU 
escolhido')
            escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 
20'), )
            escolhaL2 -= 1
            escolhaC2 = int(input('insira a coluna da segunda parte, de 1 até 20'),
)
            escolhaC2 -= 1
            while matriz[escolhaL2][escolhaC2] == 1:
                print('Número inválido, insira novamente um número que não esta 
ocupado OU escolhido')
                escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 
20'), )
                escolhaL2 -= 1
                escolhaC2 = int(input('insira a coluna da segunda parte, de 1 até 
20'), )
                escolhaC2 -= 1
        while escolhaC2 < escolhaC and escolhaL2 == escolhaL and (
                escolhaC - 3) < 0 or escolhaL2 < escolhaL and escolhaC2 == escolhaC
and (
                escolhaL - 3) < 0 or escolhaC2 > escolhaC and escolhaL2 == escolhaL
and (
                escolhaC + 4) > num or escolhaL2 > escolhaL and escolhaC2 == 
escolhaC and (escolhaL + 4) > num:
            print('escolha invalida; posição ultrapassa a borda do campo')
            escolhaL = int(input('insira a linha da primeira parte, de 1 até 
20'), )
            escolhaL -= 1
            escolhaC = int(input('insira a coluna da primeira parte, de 1 até 20'),
)
            escolhaC -= 1
            while matriz[escolhaL][escolhaC] == 1:
                print('Número inválido, insira novamente um número que não esta 
ocupado ao escolhido')
                escolhaL = int(input('insira a linha da primeira parte, de 1 até 
20'), )
                escolhaL -= 1
                escolhaC = int(input('insira a coluna da primeira parte, de 1 até 
20'), )
                escolhaC -= 1
            escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 
20'), )
            escolhaL2 -= 1
            escolhaC2 = int(input('insira a coluna da segunda parte, de 1 até 20'),
)
            escolhaC2 -= 1
            while matriz[escolhaL2][escolhaC2] == 1:
                print('Número inválido, insira novamente um número que não esta 
ocupado OU escolhido')
                escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 
20'), )
                escolhaL2 -= 1
                escolhaC2 = int(input('insira a coluna da segunda parte, de 1 até 
20'), )
                escolhaC2 -= 1
                while escolhaL2 != (escolhaL - 1) and escolhaL2 != (
                        escolhaL + 1) and escolhaL2 != escolhaL or escolhaC2 != 
(escolhaC - 1) and escolhaC2 != (
                        escolhaC + 1) and escolhaC2 != escolhaC or escolhaC2 != 
escolhaC and escolhaL2 != escolhaL or escolhaL2 == escolhaL and escolhaC2 == 
escolhaC:
                    print('Número inválido, insira novamente um número adjacente OU
escolhido')
                    escolhaL2 = int(input('insira a linha da segunda parte, de 1 
até 20'), )
                    escolhaL2 -= 1
                    escolhaC2 = int(input('insira a coluna da segunda parte, de 1 
até 20'), )
                    escolhaC2 -= 1
            while escolhaL2 != (escolhaL - 1) and escolhaL2 != (
                    escolhaL + 1) and escolhaL2 != escolhaL or escolhaC2 != 
(escolhaC - 1) and escolhaC2 != (
                    escolhaC + 1) and escolhaC2 != escolhaC or escolhaC2 != 
escolhaC and escolhaL2 != escolhaL or escolhaL2 == escolhaL and escolhaC2 == 
escolhaC:
                print('Número inválido, insira novamente um número adjacente OU 
escolhido')
                escolhaL2 = int(input('insira a linha da segunda parte, de 1 até 
20'), )
                escolhaL2 -= 1
                escolhaC2 = int(input('insira a coluna da segunda parte, de 1 até 
20'), )
                escolhaC2 -= 1
                while matriz[escolhaL2][escolhaC2] == 1:
                    print('Número inválido, insira novamente um número que não esta
ocupado OU escolhido')
                    escolhaL2 = int(input('insira a linha da segunda parte, de 1 
até 20'), )
                    escolhaL2 -= 1
                    escolhaC2 = int(input('insira a coluna da segunda parte, de 1 
até 20'), )
                    escolhaC2 -= 1
        if escolhaC2 == escolhaC and (escolhaL + 4) > num and escolhaL2 > escolhaL 
or escolhaL2 == escolhaL and (
                escolhaC + 4) > num and escolhaC2 > escolhaC or escolhaL2 == 
escolhaL and (
                escolhaC - 3) < 0 and escolhaC2 < escolhaC or escolhaC2 == escolhaC
and (
                escolhaL - 3) < 0 and escolhaL2 < escolhaL:
            if escolhaC2 == escolhaC and matriz[(escolhaL + 2)][escolhaC2] == 1 and
escolhaL2 > escolhaL:
                print(
                    'posição inválida pois a terceira parte esta ocupada; observe o
campo e escolha um lugar com espaço para 3 partes alinhadas')
            elif escolhaL2 == escolhaL and matriz[escolhaL2][escolhaC + 2] == 1 and
escolhaC2 > escolhaC:
                print(
                    'posição inválida pois a terceira parte esta ocupada; observe o
campo e escolha um lugar com espaço para 3 partes alinhadas')
            elif escolhaC2 == escolhaC and matriz[(escolhaL - 2)][escolhaC2] == 1 
and escolhaL2 < escolhaL:
                print(
                    'posição inválida pois a terceira parte esta ocupada; observe o
campo e escolha um lugar com espaço para 3 partes alinhadas')
            elif escolhaL2 == escolhaL and matriz[escolhaL2][escolhaC - 2] == 1 and
escolhaC2 < escolhaC:
                print(
                    'posição inválida pois a terceira parte esta ocupada; observe o
campo e escolha um lugar com espaço para 3 partes alinhadas')
            if escolhaC2 == escolhaC and matriz[(escolhaL + 3)][escolhaC2] == 1 and
escolhaL2 > escolhaL:
                print(
                    'posição inválida pois a quarta parte esta ocupada; observe o 
campo e escolha um lugar com espaço para 3 partes alinhadas')
            elif escolhaL2 == escolhaL and matriz[escolhaL2][escolhaC + 3] == 1 and
escolhaC2 > escolhaC:
                print(
                    'posição inválida pois a quarta parte esta ocupada; observe o 
campo e escolha um lugar com espaço para 3 partes alinhadas')
            elif escolhaC2 == escolhaC and matriz[(escolhaL - 3)][escolhaC2] == 1 
and escolhaL2 < escolhaL:
                print(
                    'posição inválida pois a quarta parte esta ocupada; observe o 
campo e escolha um lugar com espaço para 3 partes alinhadas')
            elif escolhaL2 == escolhaL and matriz[escolhaL2][escolhaC - 3] == 1 and
escolhaC2 < escolhaC:
                print(
                    'posição inválida pois a quarta parte esta ocupada; observe o 
campo e escolha um lugar com espaço para 3 partes alinhadas')
        else:
            loop -= 1
    for cont2 in range(linhas):
        if escolhaL == cont2:
            for cont3 in range(colunas):
                if escolhaC == cont3:
                    matriz[cont2][cont3] += 1
        if escolhaL2 == cont2:
            for cont4 in range(colunas):
                if escolhaC2 == cont4:
                    matriz[cont2][cont4] += 1
    for cont2 in range(linhas):
        if escolhaL == cont2:
            for cont3 in range(colunas):
                if escolhaC == cont3:
                    matriz3[cont2][cont3] += (cont + 10)
        if escolhaL2 == cont2:
            for cont4 in range(colunas):
                if escolhaC2 == cont4:
                    matriz3[cont2][cont4] += (cont + 10)
    if escolhaL == escolhaL2 and escolhaC2 > escolhaC:
        matriz[escolhaL][(escolhaC + 2)] += 1
    elif escolhaC == escolhaC2 and escolhaL2 > escolhaL:
        matriz[(escolhaL + 2)][escolhaC] += 1
    elif escolhaC == escolhaC2 and escolhaL2 < escolhaL:
        matriz[(escolhaL - 2)][escolhaC] += 1
    elif escolhaL == escolhaL2 and escolhaC2 < escolhaC:
        matriz[escolhaL][escolhaC - 2] += 1
    if escolhaL == escolhaL2 and escolhaC2 > escolhaC:
        matriz[escolhaL][(escolhaC + 3)] += 1
    elif escolhaC == escolhaC2 and escolhaL2 > escolhaL:
        matriz[(escolhaL + 3)][escolhaC] += 1
    elif escolhaC == escolhaC2 and escolhaL2 < escolhaL:
        matriz[(escolhaL - 3)][escolhaC] += 1
    elif escolhaL == escolhaL2 and escolhaC2 < escolhaC:
        matriz[escolhaL][escolhaC - 3] += 1
    if escolhaL == escolhaL2 and escolhaC2 > escolhaC:
        matriz3[escolhaL][(escolhaC + 2)] += (cont + 10)
    elif escolhaC == escolhaC2 and escolhaL2 > escolhaL:
        matriz3[(escolhaL + 2)][escolhaC] += (cont + 10)
    elif escolhaC == escolhaC2 and escolhaL2 < escolhaL:
        matriz3[(escolhaL - 2)][escolhaC] += (cont + 10)
    elif escolhaL == escolhaL2 and escolhaC2 < escolhaC:
        matriz3[escolhaL][escolhaC - 2] += (cont + 10)
    if escolhaL == escolhaL2 and escolhaC2 > escolhaC:
        matriz3[escolhaL][(escolhaC + 3)] += (cont + 10)
    elif escolhaC == escolhaC2 and escolhaL2 > escolhaL:
        matriz3[(escolhaL + 3)][escolhaC] += (cont + 10)
    elif escolhaC == escolhaC2 and escolhaL2 < escolhaL:
        matriz3[(escolhaL - 3)][escolhaC] += (cont + 10)
    elif escolhaL == escolhaL2 and escolhaC2 < escolhaC:
        matriz3[escolhaL][escolhaC - 3] += (cont + 10)
    for cont2 in range(linhas):
        print(matriz[cont2])
print('jogador 2, escolha os quadrados a serem atacados:')
loop = 1
print('caso queira parar, insira 50 na linha ou coluna')
for cont in range(colunas):
    for cont2 in range(3):
        if matriz3[cont].count((cont2 + 10)) > 3:
            condicao[cont][(cont2 + 10)] = 1
for cont in range(colunas):
    for cont2 in range(4):
        if matriz3[cont].count((cont2 + 6)) > 2:
            condicao[cont][(cont2 + 6)] = 1
for cont in range(colunas):
    for cont2 in range(5):
        if matriz3[cont].count((cont2 + 1)) > 1:
            condicao[cont][(cont2 + 1)] = 1
for cont in range(colunas):
    for cont2 in range(5):
        if matriz3[cont].count((cont2 + 1)) == 1 and (cont + 1 <= 20):
            if matriz3[(cont + 1)].count((cont2 + 1)) == 1:
                condicao2[cont][(cont2 + 1)] = 1
for cont in range(colunas):
    for cont2 in range(4):
        if matriz3[cont].count((cont2 + 6)) == 1 and (cont + 1 <= 20):
            if matriz3[cont].count((cont2 + 6)) == 1 and (cont + 2 <= 20):
                if matriz3[(cont + 1)].count((cont2 + 6)) == 1:
                    condicao2[cont][(cont2 + 6)] = 1
for cont in range(colunas):
    for cont2 in range(3):
        if matriz3[cont].count((cont2 + 10)) == 1 and (cont + 1 < 20):
            if matriz3[cont].count((cont2 + 10)) == 1 and (cont + 2 < 20):
                if matriz3[cont].count((cont2 + 10)) == 1 and (cont + 3 <= 20):
                    if matriz3[(cont + 1)].count((cont2 + 10)) == 1:
                        condicao2[cont][(cont2 + 10)] = 1
while loop == 1:
    escolhaL = int(input('Linha: '), )
    escolhaL -= 1
    if escolhaL == 49:
        loop = 0
    escolhaC = int(input('Coluna: '), )
    escolhaC -= 1
    if escolhaC == 49:
        loop = 0
    if loop != 0:
        if matriz[escolhaL][escolhaC] == 1:
            print('acertou!')
            matriz[escolhaL][escolhaC] == 0
            matriz2[escolhaL][escolhaC] = 8
            matriz3[escolhaL][escolhaC] = 0
            for cont in range(colunas):
                for cont2 in range(5):
                    if matriz3[cont].count((cont2 + 1)) == 0 and condicao[cont]
[(cont2 + 1)] == 1:
                        pontuacao += 10
                        condicao[cont][(cont2 + 1)] = 0
                        print('fragata caiu!')
            for cont in range(colunas):
                for cont2 in range(4):
                    if matriz3[cont].count((cont2 + 6)) == 0 and condicao[cont]
[(cont2 + 6)] == 1:
                        pontuacao += 20
                        condicao[cont][(cont2 + 6)] = 0
                        print('cruzador caiu!')
            for cont in range(colunas):
                for cont2 in range(3):
                    if matriz3[cont].count((cont2 + 10)) == 0 and condicao[cont]
[(cont2 + 10)] == 1:
                        pontuacao += 30
                        condicao[cont][(cont2 + 10)] = 0
                        print('porta-avioes caiu!')
            for cont in range(colunas):
                for cont2 in range(5):
                    if matriz3[cont].count((cont2 + 1)) == 1 and (cont + 1 <= 20):
                        if matriz3[(cont + 1)].count((cont2 + 1)) == 1 and 
condicao2[cont][(cont2 + 1)] == 1:
                            pontuacao += 10
                            condicao2[cont][(cont2 + 1)] = 0
                            print('fragata caiu!') 
            for cont in range(colunas):
                for cont2 in range(4):
                    if matriz3[cont].count((cont2 + 6)) == 1 and (cont + 1 <= 20):
                        if matriz3[cont].count((cont2 + 6)) == 1 and (cont + 2 <= 
20):
                            if matriz3[(cont + 1)].count((cont2 + 6)) == 1 and 
condicao2[cont][(cont2 + 6)] == 1:
                                pontuacao += 20
                                condicao2[cont][(cont2 + 6)] = 0
                                print('cruzador caiu!')
            for cont in range(colunas):
                for cont2 in range(3):
                    if matriz3[cont].count((cont2 + 10)) == 1 and (cont + 1 < 20):
                        if matriz3[cont].count((cont2 + 10)) == 1 and (cont + 2 < 
20):
                            if matriz3[cont].count((cont2 + 10)) == 1 and (cont + 3
<= 20):
                                if matriz3[(cont + 1)].count((cont2 + 10)) == 1 and
condicao2[cont][(cont2 + 10)] == 1:
                                    pontuacao += 30
                                    condicao2[cont][(cont2 + 10)] = 0
                                    print('porta-avioes caiu!')
        elif matriz[escolhaL][escolhaC] == 0:
            print('errou!')
            matriz2[escolhaL][escolhaC] = 4
        for cont in range(linhas):
            print(matriz2[cont])
            if matriz[cont].count(1) == 0:
                fimloop += 1
            if fimloop == 20:
                loop -= 1
            else:
                fimloop = 0
print(pontuacao)
