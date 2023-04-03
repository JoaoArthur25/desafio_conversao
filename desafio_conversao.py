escolhaConvertida = int(input("Escolha uma base para ser convertida: "
                              "1.Decimal / 2.Binária / 3.Octal / 4.Hexadecimal"))

while True:
    if escolhaConvertida not in [1, 2, 3, 4]:
        print("Escolha inválida. Digite uma opção de 1 a 4.")
        escolhaConvertida = int(input("Escolha uma base para ser convertida: "
                                      "1.Decimal / 2.Binária / 3.Octal / 4.Hexadecimal"))
    else:
        break

match escolhaConvertida:
    case 1:
        while True:
            escolhaConverter = int(input("Escolha uma base para converter: 1.Binária / 2.Octal / 3.Hexadecimal"))

            match int(escolhaConverter):
                case 1:
                    numDec = float(input("Digite um número:"))
                    decInt = int(numDec)
                    decFloat = numDec - decInt
                    binInt = bin(decInt)[2:]
                    binFloat = ''
                    while decFloat > 0 and len(binFloat) < 6:
                        decFloat *= 2
                        if decFloat >= 1:
                            binFloat += "1"
                            decFloat -= 1
                        else:
                            binFloat += "0"

                    numBin = binInt + '.' + binFloat
                    print(f"O número {numDec} em binário é: {numBin}")
                    break
                case 2:
                    numDec = float(input("Digite um número:"))
                    decInt = int(numDec)
                    decFloat = numDec - decInt
                    octInt = oct(decInt)[2:]
                    octFloat = ''
                    while decFloat > 0 and len(octFloat) < 6:
                        decFloat *= 8
                        if decFloat >= 8:
                            decDigit = int(decFloat/8)
                            octFloat += str(decDigit)
                            decFloat -= decDigit * 8
                        else:
                            decDigit = int(decFloat)
                            octFloat += str(decDigit)
                            decFloat -= decDigit
                    numOct = octInt + '.' + octFloat
                    print(f"{numDec} em octal é: {numOct}")
                    break
                case 3:
                    numDec = float(input("Digite um número:"))
                    decInt = int(numDec)
                    decFloat = numDec - decInt
                    hexInt = format(decInt, 'X')
                    hexFloat = ''
                    while decFloat > 0 and len(hexFloat) < 6:
                        decFloat *= 16
                        hexDigit = int(decFloat)
                        if hexDigit < 10:
                            hexFloat += str(hexDigit)
                        else:
                            hexFloat += chr(hexDigit + 55)
                        decFloat -= hexDigit
                    numHex = hexInt + '.' + hexFloat
                    print(f"O número {numDec} em hexadecimal é: {numHex}")
                    break
                case _:
                    print("Escolha inválida.")

    case 2:
        while True:
            escolhaConverter = int(input("Escolha uma base para converter: 1.Decimal / 2.Octal / 3.Hexadecimal"))
            match int(escolhaConverter):
                case 1:
                    numBin = (input("Digite um número:"))
                    numDec = int(numBin, 2)
                    print(f"{numBin} em decimal é: {numDec}")
                    break
                case 2:
                    numBin = (input("Digite um número:"))
                    numDec = int(numBin, 2)
                    numOct = oct(numDec)[2:]
                    print(f"{numBin} em octal é: {numOct}")
                    break
                case 3:
                    numBin = (input("Digite um número:"))
                    numDec = int(numBin, 2)
                    numHex = hex(numDec)[2:]
                    print(f"{numBin} em hexadecimal é: {numHex}")
                    break
                case _:
                    print("Escolha inválida.")
    case 3:
        while True:
            escolhaConverter = int(input("Escolha uma base para converter: 1.Decimal / 2.Binaria / 3.Hexadecimal"))
            match int(escolhaConverter):
                case 1:
                    numOct = input("Digite um número:")
                    numDec = int(numOct, 8)
                    print(f"{numOct} em decimal é: {numDec}")
                    break
                case 2:
                    numOct = (input("Digite um número:"))
                    numDec = int(numOct, 8)
                    numBin = bin(numDec)[2:]
                    print(f"{numOct} em binário é: {numBin}")
                    break
                case 3:
                    numOct = (input("Digite um número:"))
                    numDec = int(numOct, 8)
                    numHex = hex(numDec)[2:]
                    print(f"{numOct} em hexadecimal é: {numHex}")
                    break
                case _:
                    print("Escolha inválida.")
    case 4:
        while True:
            escolhaConverter = int(input("Escolha uma base para converter: 1.Decimal / 2.Binaria / 3.Octal"))
            match int(escolhaConverter):
                case 1:
                    numHex = input("Digite um número:")
                    numDec = int(numHex, 16)
                    print(f"{numHex} em decimal é: {numDec}")
                    break
                case 2:
                    numHex = input("Digite um número:")
                    numDec = int(numHex, 16)
                    numBin = bin(numDec)[2:]
                    print(f"{numHex} em binário é: {numBin}")
                    break
                case 3:
                    numHex = input("Digite um número:")
                    numDec = int(numHex, 16)
                    numOct = oct(numDec)[2:]
                    print(f"{numHex} em octal é: {numOct}")
                    break
                case _:
                    print("Escolha inválida.")
