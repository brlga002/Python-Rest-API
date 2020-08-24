from typing import Optional
from fastapi import FastAPI, HTTPException
import uvicorn

import functions as fc


app = FastAPI(
    title="Python Rest API",
    description= fc.description_api(),    
    version="1.0.0",
    openapi_tags=fc.tags_metadata(),
    docs_url="/",
    redoc_url="/documentationOnly")


@app.post("/soma", tags=["soma"])
def soma_de_binarios(fistNumber: Optional[str], secondNumber: Optional[str]):
    dadosValidos = fc.verifica_operacao_permitida(fistNumber, secondNumber)
    fistNumber = dadosValidos[0]
    secondNumber = dadosValidos[1]
    result = int(fistNumber + secondNumber)
    return fc.formata_zero_esquerda(bin(result))


@app.post("/subtracao", tags=["subtracao"])
def subtracao_de_binarios(fistNumber: Optional[str],
                          secondNumber: Optional[str]):
    dadosValidos = fc.verifica_operacao_permitida(fistNumber, secondNumber)
    fistNumber = dadosValidos[0]
    secondNumber = dadosValidos[1]
    fc.verifica_segundo_maior_primeiro(fistNumber, secondNumber)
    result = int(fistNumber - secondNumber)
    return fc.formata_zero_esquerda(bin(result))


@app.post("/multiplicacao", tags=["multiplicacao"])
def multiplicacao_dois_numeros_binarios(fistNumber: Optional[str],
                                        secondNumber: Optional[str]):
    dadosValidos = fc.verifica_operacao_permitida(fistNumber, secondNumber)
    fistNumber = dadosValidos[0]
    secondNumber = dadosValidos[1]
    result = int(fistNumber * secondNumber)
    return fc.formata_zero_esquerda(bin(result))


@app.post("/divisao", tags=["divisao"])
def divisao_dois_numeros_binarios(fistNumber: Optional[str],
                                  secondNumber: Optional[str]):
    dadosValidos = fc.verifica_operacao_permitida(fistNumber, secondNumber)
    fistNumber = dadosValidos[0]
    secondNumber = dadosValidos[1]
    fc.verifica_segundo_maior_primeiro(fistNumber, secondNumber)
    result = bin(int(fistNumber / secondNumber))

    if (fistNumber % secondNumber != 0):
        result = fc.gera_binario_depois_float(fistNumber, secondNumber)

    return fc.formata_zero_esquerda(result)


@app.post("/resto", tags=["resto"])
def resto_da_divisao_dois_numeros_binarios(fistNumber: Optional[str],
                                           secondNumber: Optional[str]):
    dadosValidos = fc.verifica_operacao_permitida(fistNumber, secondNumber)
    fistNumber = dadosValidos[0]
    secondNumber = dadosValidos[1]
    fc.verifica_segundo_maior_primeiro(fistNumber, secondNumber)
    result = int(fistNumber % secondNumber)
    return fc.formata_zero_esquerda(bin(result))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)    