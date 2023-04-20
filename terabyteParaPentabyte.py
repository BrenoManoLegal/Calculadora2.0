def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def terabyteParaPentabyte(valorASerConvertido):
    print('Valor convertido de terabyte para Pentabyte')
    bytesCalculado = valorASerConvertido / 1024
    return bytesCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = terabyteParaPentabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)
