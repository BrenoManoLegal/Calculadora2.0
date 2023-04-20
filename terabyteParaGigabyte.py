def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def terabyteParaGigabyte(valorASerConvertido):
    print('Valor convertido de terabyte para Gigabyte')
    bytesCalculado = valorASerConvertido * 1024
    return bytesCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = terabyteParaGigabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)