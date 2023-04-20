def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def kilobyteParaByte(valorASerConvertido):
    print('Valor convertido de Kilobyte para Byte')
    bytesCalculado = valorASerConvertido * 1024
    return bytesCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = kilobyteParaByte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)