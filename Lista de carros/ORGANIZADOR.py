import os

def organiza():
    with open('lista.txt', 'r') as lista:
        with open('insercaoPPM.txt', 'w') as  isr:
            texto = lista.readlines()
            texto.sort()
            for item in texto:
                item = item.strip('\n').upper()
                if " " in item:
                    isr.write(f'"{item}",')
                else:
                    isr.write(item + ',')
    input('''
                TUDO CERTO !
                ''')
while True:
    if input('''
      ADICIONE A MARCA OU MODELO NO ARQUIVO LISTA.TXT SALVO DENTRO DA MESMA PASTA DESSE EXECUTAVEL.
      O PROGRAMA CRIARA UMA LISTA PRONTA PARA SER INSERIDA NO MANAGER NO ARQUIVO INSERCAOPPM.TXT.
            
      PRESIONE <ENTER> PARA CONTINUAR <S> para sair
      
      ''').upper() == 'S':
        break
    else:
        try:
            organiza()
            os.system('cls')
            break
        except FileNotFoundError:
            input('''
                ARQUIVO 'LISTAS.TXT' NAO ENCONTRADO
                ''')
            os.system('cls')
        except:
            input('''
            ERRO DESCONHECIDO
            ''')
            os.system('cls')
               