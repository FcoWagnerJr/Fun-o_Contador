# Fun-o_Contador
📈 Função `maior()` - Identificador de Maior Valor

📌 Visão Geral
Função Python que analisa números em tempo real e identifica o maior valor de uma sequência, com saída formatada.

🛠️ Como Funciona
```
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
    
    # Saída formatada
    print(f', Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi: {maior}.')
    print('---'*30)  
```

## 🎯 Funcionalidades
- ✅ Análise em tempo real com efeito visual (`sleep(0.3)`)
- ✅ Contagem automática de valores
- ✅ Identificação do maior número
- ✅ Saída organizada com separadores
- ✅ Funciona com qualquer quantidade de argumentos (0 a N)

📊 Exemplos Práticos
```python
maior(3, 9, 5, 6, 8, 1)  # Análise de 6 números
maior(4, 8, 0)           # Análise de 3 números
maior(1, 2)              # Análise de 2 números
maior(6)                 # Análise de 1 número
maior()                  # Chamada sem argumentos
```
🖥️ Saída para o usuário
```
Analisando os números passados... 
3 9 5 6 8 1 , Foram informados 6 valores ao todo.
O maior valor informado foi: 9.
------------------------------

Analisando os números passados... 
4 8 0 , Foram informados 3 valores ao todo.
O maior valor informado foi: 8.
------------------------------

>>> Fim da execução <<<
```

💡 Casos Especiais
- Quando chamada sem argumentos (`maior()`), retorna contagem zero
- Mantém formatação consistente em todas as execuções

🚀 Como Utilizar
1. Copie a função para seu código Python
2. Chame `maior()` com seus números como argumentos
3. Veja o resultado formatado no console

📦 Tecnologias:
- Python 3
- Módulo `time` (padrão da biblioteca Python)
