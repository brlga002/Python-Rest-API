from fastapi import HTTPException


def tags_metadata():
    tags_metadata = [
        {
            "name": "soma",
            "description": "Soma entre dois números binários",
        },
        {
            "name": "subtracao",
            "description": "Subtração entre dois números binários",
        },
        {
            "name": "multiplicacao",
            "description": "Multiplicação entre dois números binários",
        },
        {
            "name": "divisao",
            "description": "Divisão entre dois números binários",
        },
        {
            "name": "resto",
            "description": "Resto da divisão entre dois números binários",
        },
    ]
    return tags_metadata

def description_api():
    description = ''' 
        Teste para vaga Desenvolvedor Home Office na Digistarts disponível no repositório: 
        <a href=\"https://github.com/brlga002/Python-Rest-API\" target=\"_blank\">Python Rest API</a>  
        Uma versão em note está em <a href=\"https://github.com/brlga002/digistarts\" target=\"_blank\">digistarts</a>'''
    return description

def verifica_operacao_permitida(fistNumber, secondNumber):
    try:
        fistNumber = int(fistNumber, 2)
        secondNumber = int(secondNumber, 2)
    except:
        raise HTTPException(
            status_code=400,
            detail="O fistNumber e secondNumber deve ser binário")

    if (fistNumber > 255 or fistNumber < 0):
        raise HTTPException(
            status_code=400,
            detail="O fistNumber número deve ser entre 0 e 255")

    if (secondNumber > 255 or secondNumber < 0):
        raise HTTPException(
            status_code=400,
            detail="O secondNumber número deve ser entre 0 e 255")

    return [fistNumber, secondNumber]


def verifica_segundo_maior_primeiro(fistNumber, secondNumber):
    if (secondNumber > fistNumber):
        raise HTTPException(
            status_code=400,
            detail=
            "O segundo número não pode ser maior que o primeiro nesta operação"
        )


def formata_zero_esquerda(number):
    return number.replace('0b', '').rjust(8, '0')


def gera_binario_depois_float(fistNumber, secondNumber):
    resultadoSomaFloat = float(fistNumber / secondNumber)
    inteiro, decimal = str(resultadoSomaFloat).split('.')
    inteiroInBytes = bin(int(inteiro))

    decimal_list = []
    counter = 0
    digits_precison = 8 - len(inteiroInBytes)

    while (counter <= digits_precison):
        if (decimal != "0"):
            x = float('0.' + decimal) * 2
            sobra, decimal = str(x).split('.')
            decimal_list.append(sobra)
        counter += 1

    decimalInBytes = ''
    for i in decimal_list:
        decimalInBytes += i

    return inteiroInBytes + '.' + decimalInBytes
