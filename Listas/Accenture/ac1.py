def main():
    meses31 = [1,3,5,7,8,10,12]
    meses30 = [4,6,9,11]
    numeroDias = 0
    diaInformado = 7
    mesInformado = 9
    anoInformado = 1992
    Index = 0
    while Index < 7:
        if mesInformado == meses31[Index]:
            numeroDias = 31*(mesInformado-1)+diaInformado
        Index += 1
    Index = 0
    while Index < 4:
        if mesInformado == meses30[Index]:
            numeroDias = 30*(mesInformado-1) + diaInformado
        Index += 1
    if mesInformado > 2:
        numeroDias = numeroDias + 1
    if mesInformado == 2:
        numeroDias = 31 + diaInformado
    print(numeroDias)

    




main()


