def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def megabyteParaGigabyte(valorASerConvertido):
    print('Valor convertido de megabyte para Gigabyte')
    bytesCalculado = valorASerConvertido * 1024
    return bytesCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = megabyteParaGigabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)