def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def kilobyteParaMegabyte(valorASerConvertido):
    print('Valor convertido de kilobyte para Megabyte')
    bytesCalculado = valorASerConvertido / 1024
    return bytesCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = kilobyteParaMegabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)