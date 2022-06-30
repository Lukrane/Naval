# meh
batalha naval + ou -
o objetivo do trabalho era programas batalha naval em python, com algumas especificações
1. apenas um tabuleiro seria necessario (a ideia seria: um jogador posiciona as peças, e outro as ataca, sem intercalar a vez)
2. as peças seriam posicionadas horizontalmente
3. seria obrigatório o uso de funções
bem, olhando pra trás ja começa a dar uma raiva de mim, ja que dessas 3 condições, eu só cumpri uma
primeiro eu interpretei duas coisas erradas: as condições 2 e 3
achei que a posição deveria ser OPCIONAL do jogador, e não apenas na horizantal
isso acabou dificultando muito as coisas, e deixou o processo de posicionar as peças muito mais trabalhoso pro usuario 
(12 peças por sinal; 
5 de 2 pedaços,
4 de 3 pedaços,
e 3 de 4 pedaços)
e o outro: funções
por algum motivo, pensei que utilizar funções era PROIBIDO, o exato contrário do que realmente era
o pior era enquanto programava, ficava pensando o quão mais fácil seria se utilizar funções fosse permitido
a lógica do meu monstro de frankenstein foi simples
uma matriz armazena os valores das peças posicionadas
o usuario posiciona pedaço por pedaço, o que tornou o processo bem pior do que precisava
começando pelos de 5 barcos de 2 pedaços, depois os de 3 e terminando com os de 4 pedaços, 12 no total
tecnicamente não era tão ruim quanto parece, pois para os de 3 e 4 pedaços, só era necessário escolher os 2 primeiros pedaços, 
depois o codigo atraves de ifs e elifs identifica a orientação e direção da peça e coloca os ultimos pedaços
com isso também foi necessario implementar uma condição pra impedir que o usuario posicione peças que iriam ultrapassar a borda
outra coisa importante é permitir o usuario posicionar o segundo pedaço apenas se ele for horizaontalmente ou verticalmente adjacente ao primeiro
por fim, a parte da pontuação
os de 2 pedaços valiam 10 pontos
os de 3 valiam 20
e os de 4, 30
porem só seria disponibilizada a pontuação caso o barco inteiro fosse destruido
pra identificar isso, uma outra matriz armazenava os valores das posições de cada barco com um numero na matriz
(barco 1 seria marcado com 1, barco 2 com 2, assim até o 12)
os 5 primeiros seriam os de 10 pontos
6 até 9 os de 20
e os ultimos 3 os de 30
depois de cada tiro, um for procura essa matriz inteira pra verificar se esses grupos de números foram completamente removidos
por exemplo, caso todos os numeros "6" tenham desaparecido da matriz, o for identifica que um barco de 3 pedaços foi destruido e da 20 pontos
o for verifica de mais de uma maneira também
uma na vertical (se o numero não tiver um numero identico na vertical, ele esta na vertical)
e uma na horizaontal (se o número tiver um número identico adjacente na horizontal, ele esta na horizontal)
foi definitivamente um projeto
a conclusão foi... algo
