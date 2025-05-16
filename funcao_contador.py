from time import sleep
def maior(*num):
    cont = maior = 0
    print('\nAnalisando os números passados... ')
    for valor in num:
        print(f'{valor} ', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f', Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi: {maior}.')
    print('---'*30)

    
maior(3, 9, 5, 6, 8, 1)
maior(4, 8, 0)
maior(1, 2)
maior(6)
maior()
print('>>> Fim da execução <<<')
