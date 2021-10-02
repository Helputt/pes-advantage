#Rodadas de Vantagem para ser campeão

#função
def antecipa(rod,pts1,pts2,tim1,tim2):
    while (rod>0):
        pts1 += 3
        pts2 += 3
        rod -= 1
    #Exibição dos pontos finais
    print('Vencendo todas,',tim1,'tem',pts1,'pontos no final!')
    print('Vencendo todas,',tim2,'tem',pts2,'pontos no final!')
    van = pts1 - pts2
    if (van==10):
        ant = (van/3)
        #Exibição rodadas de antecedência
        if ant<1:
            print(tim1,'terá',van,'pontos de vantagem, precisando decidir na última rodada. '
            'Haja coração, amigo!')
        elif ant>=3:
            print(tim1,'terá',van,'pontos de vantagem, ganhando com ',"%.f" % ant, 'rodadas '
            'de antecedência. Tem uma gordurinha boa pra queimar!')
        else:
           print(tim1,'terá',van,'pontos de vantagem, ganhando com ',"%.f" % ant, 'rodadas '
            'de antecedência!')
    else:
        #Acertar valor para o arredondamento
        ant = (van/3)-1
        if ant<1:
            print(tim1,'terá',van,'pontos de vantagem, precisando decidir na última rodada. '
            'Haja coração, amigo!')
        elif ant>=3:
            print(tim1,'terá',van,'pontos de vantagem, ganhando com ',"%.f" % ant, 'rodadas '
            'de antecedência. Tem uma gordurinha boa pra queimar!')
        else:
            print(tim1,'terá',van,'pontos de vantagem, ganhando com ',"%.f" % ant, 'rodadas '
            'de antecedência!')
    
#Entrada das variáveis
rod=int(input('Informe quantas rodadas faltam: '))
tim1=str(input('Informe o nome do time primeiro colocado: '))
tim2=str(input('Informe o nome do time segundo colocado: '))
pts1=int(input('Informe quantos pontos o primeiro colocado tem: '))
pts2=int(input('Informe quantos pontos o segundo colocado tem: '))

#Chamando Função
antecipa(rod,pts1,pts2,tim1,tim2)
         
