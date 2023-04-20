def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def gigabyteParaMegabyte(valorASerConvertido):
    print('Valor convertido de gigabyte para Megabyte')
    bytesCalculado = valorASerConvertido * 1024
    return bytesCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = gigabyteParaMegabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)