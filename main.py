print('''

.OOOOOOOOOOOOOOO @@         D i c k  T r a c y        @@ OOOOOOOOOOOOOOOO.
OOOOOOOOOOOOOOOO @@                                    @@ OOOOOOOOOOOOOOOO
OOOOOOOOOO'''
      ''' @@                                    @@ ```````OOOOOOOOO
OOOOO'' aaa@@@@@@@@@@@@@@@@@@@@"""                   """""""""@@aaaa `OOOO
OOOOO,""""@@@@@@@@@@@@@@""""                                     a@"" OOOA
OOOOOOOOOoooooo,                                            |OOoooooOOOOOS
OOOOOOOOOOOOOOOOo,            I'll be selling the           |OOOOOOOOOOOOC
OOOOOOOOOOOOOOOOOO            house and moving my          ,|OOOOOOOOOOOOI
OOOOOOOOOOOOOOOOOO @           family to a condo           |OOOOOOOOOOOOOI
OOOOOOOOOOOOOOOOO'@           complex with a pool          OOOOOOOOOOOOOOb
OOOOOOOOOOOOOOO'a'            & where someone else         |OOOOOOOOOOOOOy
OOOOOOOOOOOOOO''              mows the grass!           aa`OOOOOOOOOOOP
OOOOOOOOOOOOOOb,..            Things here will be           `@aa``OOOOOOOh
OOOOOOOOOOOOOOOOOOo           hectic for the next             `@@@aa OOOOo
OOOOOOOOOOOOOOOOOOO|          6 weeks or so.                     @@@ OOOOe
OOOOOOOOOOOOOOOOOOO@                               aaaaaaa       @@',OOOOn
OOOOOOOOOOOOOOOOOOO@                        aaa@@@@@@@@""        @@ OOOOOi
OOOOOOOOOO~~ aaaaaa"a                 aaa@@@@@@@@@@""            @@ OOOOOx
OOOOOO aaaa@"""""""" ""            @@@@@@@@@@@@""               @@@|`OOOO'
OOOOOOOo`@@a                  aa@@  @@@@@@@""         a@        @@@@ OOOO9
OOOOOOO'  `@@a               @@a@@   @@""           a@@   a     |@@@ OOOO3
`OOOO'       `@    aa@@       aaa"""          @a        a@     a@@@',OOOO'
***************************************************************************
''')
print("Bem-vindo ao Detetive Zapo.")
print("Sua missão é encontrar o assassino.")
input('Estranho: Eu vi um homem entrando pela porta dos fundos ele parecia estar de avental... "Aperte Enter para continuar"\n')

choice1 = input('Locutor: Em sua esquerda está um Restaurante, e em sua direita uma Escola. Escolha "Direita" ou "esquerda".\n').lower()
if choice1 == "esquerda":
  choice2 = input('Você entrou no restaurante e encontrou um homem morto, você tem duas opções... ir para a Cozinha ou checar o estacionamento. Digite "Cozinha" ou "Estacionamento".\n').lower()
  if choice2 == "cozinha":
    choice3 = input('Você encontra três cozinheiros com o avental sujo. Um estava sujo de "Verde" outro "Vermelho" e outro "Preto". Escolha uma cor \n').lower()
    if choice3 == "verde":
      print("Você prendeu o cozinheiro errado! Seu avental era molho verde!")
    elif choice3 == "vermelho":
      print("Parabéns, você prendeu o cozinheiro certo! Seu avental estava sujo de sangue!")
    elif choice3 == "preto":
      print("Você prendeu o cozinheiro errado! Seu avental era Shoyo!")
    else:
      print("Você escolheu o lado errado.")
  else:
    print("Você se perdeu no estacionamento e deixou o assassino escapar!")
else:
  print("A escola estava fechada. O assassino escapou!")