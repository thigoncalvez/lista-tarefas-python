import os

lista = []

while True:
    print('selecione uma opcao:')
    opcao = input('[i]nserir,[a]pagar,[l]ista:')

    if opcao == 'i':
        os.system('cls')
        valor = input('valor:')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
        'escolha uma opcao para apagar')
        try :
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('digite um numero valido')
        except IndexError:
            print('valor não exixte na lista')
        except Exception:
            print("erro desconhecido")
    elif opcao == "l" :
        os.system('cls')

        if len(lista)== 0:
            print('nada para limpar')

        for i,valor in enumerate(lista):
            print(i,valor)
    else:
        print('por favor escolha i,a ou l')        