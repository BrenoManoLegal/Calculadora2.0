def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def gigabyteParaTerabyte(valorASerConvertido):
    print('Valor convertido de gigabyte para Terabyte')
    bytesCalculado = valorASerConvertido / 1024
    return bytesCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = gigabyteParaTerabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)