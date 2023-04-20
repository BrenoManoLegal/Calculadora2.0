def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def pentabyteParaTerabyte(valorASerConvertido):
    print('Valor convertido de pentabyte para Terabyte')
    bytesCalculado = valorASerConvertido * 1024
    return bytesCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = pentabyteParaTerabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)