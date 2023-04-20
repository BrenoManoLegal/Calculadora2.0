def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def megabyteParaKilobyte(valorASerConvertido):
    print('Valor convertido de megabyte para Kilobyte')
    bytesCalculado = valorASerConvertido * 1024
    return bytesCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = megabyteParaKilobyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)