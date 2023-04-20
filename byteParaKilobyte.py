def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def byteParaKilobyte(valorASerConvertido):
    print('Valor convertido de byte para Kilobyte')
    bytesCalculado = valorASerConvertido / 1024
    return bytesCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = byteParaKilobyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)